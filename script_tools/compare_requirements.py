import pandas as pd
import re


def compare_requirements(requirement1, requirement2):  # type:(str,str)->None
    """

    :param requirement1:
    :param requirement2:
    :return:
    """

    def process(requirement):  # type:(str)->pd.DataFrame
        """
        conda list head要求为：
        # Name     Version     Build     Channel
        pip list head要求为：
        Package    Version
        ----------------------------------------

        :param requirement:
        :return:
        """
        df = pd.DataFrame(columns=["name", "version"])
        with open(requirement, "r") as f:
            data = f.readlines()
            for idx, line_data in enumerate(data):
                # conda list
                if "Name" in line_data and "Version" in line_data:
                    start_line_index = idx + 1
                    break
                # pip list
                elif "Package" in line_data and "Version" in line_data:
                    start_line_index = idx + 2
                    break
                else:
                    start_line_index = None
            if start_line_index == None:
                raise ValueError("requirement.txt 格式不符合 pip list 或 conda list ！！！！")

        for line_data in data[start_line_index:]:
            line_data_list = re.findall("\S*\S", line_data.strip("\n"))
            if len(line_data_list) < 2:
                break
            df = df.append({"name": line_data_list[0], "version": line_data_list[1]}, ignore_index=True)

        return df

    df1 = process(requirement=requirement1)
    df2 = process(requirement=requirement2)

    df_res = pd.merge(df1, df2, how="outer", on="name", suffixes=("_1", "_2"))
    df_res["is_equal"] = df_res.apply(lambda row: 1 if row["version_1"] == row["version_2"] else 0, axis=1)
    df_res.to_csv("compare_result.csv", index=False)


if __name__ == '__main__':
    requirement1 = "requirement_1.txt"
    requirement2 = "requirement_2.txt"
    compare_requirements(requirement1=requirement1, requirement2=requirement2)