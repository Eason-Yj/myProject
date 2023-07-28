from jsonpath_rw_ext import parse

# from jsonpath_ng import parse

if __name__ == '__main__':
    s = [
        {
            "age": 34,
            "workclass": -1.416326648218765,
            "fnlwgt": 148291,
            "education": -2.431417964837014,
            "education_num": 9,
            "marital_status": -0.39915593891489903,
            "occupation": -1.0986122886681091,
            "relationship": -0.182321556793954,
            "race": -1.316982561229661,
            "sex": 1,
            "capital_gain": 0,
            "capital_loss": 0,
            "hours_per_week": 32,
            "native_country": 0,
            "income": "<=50K",
            "__index_level_0__": 0,
            "_binary_result": 1.0,
            "positive_prob_>50K": 0.8412698412698413,
            "probability_<=50K": 0.15873015873015872,
            "result_label": "<=50K"
        }
    ]
    # json_path_expr = parse("$[*].probability_<=50K")
    # 报错：Exception: Parse error at 1:17 near token <= (FILTER_OP)，原因是jsonpath中含有特殊字符<=
    json_path_expr = parse("$[*].result_label")
    res = json_path_expr.find(s)
    res = [i.value for i in res]
    print(res)
