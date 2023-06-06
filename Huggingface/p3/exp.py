from datasets import load_dataset
from transformers import pipeline
import os

all_data = ['adversarial_qa_dbert_answer_the_following_q', 'adversarial_qa_dbert_based_on',
            'adversarial_qa_dbert_generate_question', 'adversarial_qa_dbert_question_context_answer',
            'adversarial_qa_dbert_tell_what_it_is', 'adversarial_qa_dbidaf_answer_the_following_q',
            'adversarial_qa_dbidaf_based_on', 'adversarial_qa_dbidaf_generate_question',
            'adversarial_qa_dbidaf_question_context_answer', 'adversarial_qa_dbidaf_tell_what_it_is',
            'adversarial_qa_droberta_answer_the_following_q', 'adversarial_qa_droberta_based_on',
            'adversarial_qa_droberta_generate_question', 'adversarial_qa_droberta_question_context_answer',
            'adversarial_qa_droberta_tell_what_it_is', 'ag_news_classify', 'ag_news_classify_question_first',
            'ag_news_classify_with_choices', 'ag_news_classify_with_choices_question_first', 'ag_news_recommend',
            'ag_news_which_section', 'ag_news_which_section_choices', 'ai2_arc_ARC_Challenge_heres_a_problem',
            'ai2_arc_ARC_Challenge_i_am_hesitating', 'ai2_arc_ARC_Challenge_multiple_choice',
            'ai2_arc_ARC_Challenge_pick_false_options', 'ai2_arc_ARC_Challenge_pick_the_most_correct_option',
            'ai2_arc_ARC_Challenge_qa_options', 'ai2_arc_ARC_Easy_heres_a_problem', 'ai2_arc_ARC_Easy_i_am_hesitating',
            'ai2_arc_ARC_Easy_multiple_choice', 'ai2_arc_ARC_Easy_pick_false_options',
            'ai2_arc_ARC_Easy_pick_the_most_correct_option', 'ai2_arc_ARC_Easy_qa_options',
            'amazon_polarity_Is_this_product_review_positive', 'amazon_polarity_Is_this_review',
            'amazon_polarity_Is_this_review_negative', 'amazon_polarity_User_recommend_this_product',
            'amazon_polarity_convey_negative_or_positive_sentiment', 'amazon_polarity_flattering_or_not',
            'amazon_polarity_negative_or_positive_tone', 'amazon_polarity_user_satisfied',
            'amazon_polarity_would_you_buy', 'anli_GPT_3_style_r1', 'anli_GPT_3_style_r1_score_eval',
            'anli_GPT_3_style_r2', 'anli_GPT_3_style_r2_score_eval', 'anli_GPT_3_style_r3',
            'anli_GPT_3_style_r3_score_eval', 'anli_MNLI_crowdsource_r1', 'anli_MNLI_crowdsource_r1_score_eval',
            'anli_MNLI_crowdsource_r2', 'anli_MNLI_crowdsource_r2_score_eval', 'anli_MNLI_crowdsource_r3',
            'anli_MNLI_crowdsource_r3_score_eval', 'anli_always_sometimes_never_r1',
            'anli_always_sometimes_never_r1_score_eval', 'anli_always_sometimes_never_r2',
            'anli_always_sometimes_never_r2_score_eval', 'anli_always_sometimes_never_r3',
            'anli_always_sometimes_never_r3_score_eval', 'anli_based_on_the_previous_passage_r1',
            'anli_based_on_the_previous_passage_r1_score_eval', 'anli_based_on_the_previous_passage_r2',
            'anli_based_on_the_previous_passage_r2_score_eval', 'anli_based_on_the_previous_passage_r3',
            'anli_based_on_the_previous_passage_r3_score_eval', 'anli_can_we_infer_r1',
            'anli_can_we_infer_r1_score_eval', 'anli_can_we_infer_r2', 'anli_can_we_infer_r2_score_eval',
            'anli_can_we_infer_r3', 'anli_can_we_infer_r3_score_eval', 'anli_claim_true_false_inconclusive_r1',
            'anli_claim_true_false_inconclusive_r1_score_eval', 'anli_claim_true_false_inconclusive_r2',
            'anli_claim_true_false_inconclusive_r2_score_eval', 'anli_claim_true_false_inconclusive_r3',
            'anli_claim_true_false_inconclusive_r3_score_eval', 'anli_consider_always_sometimes_never_r1',
            'anli_consider_always_sometimes_never_r1_score_eval', 'anli_consider_always_sometimes_never_r2',
            'anli_consider_always_sometimes_never_r2_score_eval', 'anli_consider_always_sometimes_never_r3',
            'anli_consider_always_sometimes_never_r3_score_eval', 'anli_does_it_follow_that_r1',
            'anli_does_it_follow_that_r1_score_eval', 'anli_does_it_follow_that_r2',
            'anli_does_it_follow_that_r2_score_eval', 'anli_does_it_follow_that_r3',
            'anli_does_it_follow_that_r3_score_eval', 'anli_does_this_imply_r1', 'anli_does_this_imply_r1_score_eval',
            'anli_does_this_imply_r2', 'anli_does_this_imply_r2_score_eval', 'anli_does_this_imply_r3',
            'anli_does_this_imply_r3_score_eval', 'anli_guaranteed_possible_impossible_r1',
            'anli_guaranteed_possible_impossible_r1_score_eval', 'anli_guaranteed_possible_impossible_r2',
            'anli_guaranteed_possible_impossible_r2_score_eval', 'anli_guaranteed_possible_impossible_r3',
            'anli_guaranteed_possible_impossible_r3_score_eval', 'anli_guaranteed_true_r1',
            'anli_guaranteed_true_r1_score_eval', 'anli_guaranteed_true_r2', 'anli_guaranteed_true_r2_score_eval',
            'anli_guaranteed_true_r3', 'anli_guaranteed_true_r3_score_eval', 'anli_justified_in_saying_r1',
            'anli_justified_in_saying_r1_score_eval', 'anli_justified_in_saying_r2',
            'anli_justified_in_saying_r2_score_eval', 'anli_justified_in_saying_r3',
            'anli_justified_in_saying_r3_score_eval', 'anli_must_be_true_r1', 'anli_must_be_true_r1_score_eval',
            'anli_must_be_true_r2', 'anli_must_be_true_r2_score_eval', 'anli_must_be_true_r3',
            'anli_must_be_true_r3_score_eval', 'anli_should_assume_r1', 'anli_should_assume_r1_score_eval',
            'anli_should_assume_r2', 'anli_should_assume_r2_score_eval', 'anli_should_assume_r3',
            'anli_should_assume_r3_score_eval', 'anli_take_the_following_as_truth_r1',
            'anli_take_the_following_as_truth_r1_score_eval', 'anli_take_the_following_as_truth_r2',
            'anli_take_the_following_as_truth_r2_score_eval', 'anli_take_the_following_as_truth_r3',
            'anli_take_the_following_as_truth_r3_score_eval', 'app_reviews_categorize_rating_using_review',
            'app_reviews_convert_to_rating', 'app_reviews_convert_to_star_rating', 'app_reviews_generate_review',
            'cnn_dailymail_3.0.0_2_or_3_sentences', 'cnn_dailymail_3.0.0_generate_story',
            'cnn_dailymail_3.0.0_news_card_view', 'cnn_dailymail_3.0.0_news_stock', 'cnn_dailymail_3.0.0_news_summary',
            'cnn_dailymail_3.0.0_spice_up_story', 'cnn_dailymail_3.0.0_sum_in_brief',
            'cnn_dailymail_3.0.0_tldr_summary', 'cnn_dailymail_3.0.0_write_an_outline', 'common_gen_Example_prompt',
            'common_gen_Given_concepts_type_1', 'common_gen_Given_concepts_type_2', 'common_gen_Put_together',
            'common_gen_choice_in_concept_centric_sentence_generation', 'common_gen_random_task_template_prompt',
            'common_gen_sentence_to_concepts', 'common_gen_topic_to_sentence', 'common_gen_topics_from_the_sentence',
            'cos_e_v1.11_aligned_with_common_sense', 'cos_e_v1.11_description_question_option_id',
            'cos_e_v1.11_description_question_option_text', 'cos_e_v1.11_explain_why_human',
            'cos_e_v1.11_generate_explanation_given_text', 'cos_e_v1.11_i_think',
            'cos_e_v1.11_question_description_option_id', 'cos_e_v1.11_question_description_option_text',
            'cos_e_v1.11_question_option_description_id', 'cos_e_v1.11_question_option_description_text',
            'cos_e_v1.11_rationale', 'cosmos_qa_context_answer_to_question',
            'cosmos_qa_context_description_question_answer_id', 'cosmos_qa_context_description_question_answer_text',
            'cosmos_qa_context_description_question_text', 'cosmos_qa_context_question_description_answer_id',
            'cosmos_qa_context_question_description_answer_text', 'cosmos_qa_context_question_description_text',
            'cosmos_qa_description_context_question_answer_id', 'cosmos_qa_description_context_question_answer_text',
            'cosmos_qa_description_context_question_text', 'cosmos_qa_no_prompt_id', 'cosmos_qa_no_prompt_text',
            'cosmos_qa_only_question_answer', 'dbpedia_14_given_a_choice_of_categories_',
            'dbpedia_14_given_a_list_of_category_what_does_the_title_belong_to',
            'dbpedia_14_given_list_what_category_does_the_paragraph_belong_to',
            'dbpedia_14_pick_one_category_for_the_following_text', 'dream_answer_to_dialogue', 'dream_baseline',
            'dream_generate_first_utterance', 'dream_generate_last_utterance',
            'dream_read_the_following_conversation_and_answer_the_question', 'duorc_ParaphraseRC_answer_question',
            'duorc_ParaphraseRC_build_story_around_qa', 'duorc_ParaphraseRC_decide_worth_it',
            'duorc_ParaphraseRC_extract_answer', 'duorc_ParaphraseRC_generate_question',
            'duorc_ParaphraseRC_generate_question_by_answer', 'duorc_ParaphraseRC_movie_director',
            'duorc_ParaphraseRC_question_answering', 'duorc_ParaphraseRC_title_generation',
            'duorc_SelfRC_answer_question', 'duorc_SelfRC_build_story_around_qa', 'duorc_SelfRC_decide_worth_it',
            'duorc_SelfRC_extract_answer', 'duorc_SelfRC_generate_question', 'duorc_SelfRC_generate_question_by_answer',
            'duorc_SelfRC_movie_director', 'duorc_SelfRC_question_answering', 'duorc_SelfRC_title_generation',
            'gigaword_TLDR', 'gigaword_first_sentence_title', 'gigaword_generate_summary_for_this',
            'gigaword_in_a_nutshell', 'gigaword_make_a_title', 'gigaword_reverse_writing',
            'gigaword_write_a_title_for_this_sentence', 'gigaword_write_an_article', 'gigaword_write_its_sentence',
            'glue_mrpc_equivalent', 'glue_mrpc_generate_paraphrase', 'glue_mrpc_generate_sentence',
            'glue_mrpc_paraphrase', 'glue_mrpc_replace', 'glue_mrpc_same_thing', 'glue_mrpc_want_to_know',
            'glue_qqp_answer', 'glue_qqp_duplicate', 'glue_qqp_duplicate_or_not', 'glue_qqp_meaning', 'glue_qqp_quora',
            'glue_qqp_same_thing', 'hellaswag_Appropriate_continuation_Yes_or_No', 'hellaswag_Open_ended_completion',
            'hellaswag_Open_ended_start', 'hellaswag_Predict_ending_with_hint',
            'hellaswag_Predict_ending_with_hint_score_eval', 'hellaswag_Randomized_prompts_template',
            'hellaswag_Randomized_prompts_template_score_eval', 'hellaswag_Reversed_appropriate_continuation_Yes_or_No',
            'hellaswag_Topic_of_the_context', 'hellaswag_Topic_without_the_ending_answer',
            'hellaswag_complete_first_then', 'hellaswag_complete_first_then_score_eval', 'hellaswag_how_ends',
            'hellaswag_if_begins_how_continues', 'hellaswag_if_begins_how_continues_score_eval',
            'imdb_Movie_Expressed_Sentiment', 'imdb_Movie_Expressed_Sentiment_2',
            'imdb_Negation_template_for_positive_and_negative', 'imdb_Reviewer_Enjoyment',
            'imdb_Reviewer_Enjoyment_Yes_No', 'imdb_Reviewer_Expressed_Sentiment',
            'imdb_Reviewer_Opinion_bad_good_choices', 'imdb_Reviewer_Sentiment_Feeling', 'imdb_Sentiment_with_choices_',
            'imdb_Text_Expressed_Sentiment', 'imdb_Writer_Expressed_Sentiment', 'kilt_tasks_hotpotqa_combining_facts',
            'kilt_tasks_hotpotqa_complex_question', 'kilt_tasks_hotpotqa_final_exam', 'kilt_tasks_hotpotqa_formulate',
            'kilt_tasks_hotpotqa_straighforward_qa', 'multi_news_distill', 'multi_news_expand_reverse_task_',
            'multi_news_summarize', 'multi_news_summary_scenario', 'multi_news_synthesize',
            'multi_news_what_are_the_key_points', 'openbookqa_main_choices',
            'openbookqa_main_choose_an_answer_with_options', 'openbookqa_main_only_options',
            'openbookqa_main_pick_answer_with_options', 'openbookqa_main_pick_using_id',
            'openbookqa_main_which_correct', 'openbookqa_main_which_correct_inverse',
            'paws_labeled_final_Concatenation', 'paws_labeled_final_Concatenation_no_label',
            'paws_labeled_final_Meaning', 'paws_labeled_final_Meaning_no_label', 'paws_labeled_final_PAWS_ANLI_GPT3',
            'paws_labeled_final_PAWS_ANLI_GPT3_no_label', 'paws_labeled_final_Rewrite',
            'paws_labeled_final_Rewrite_no_label', 'paws_labeled_final_context_question',
            'paws_labeled_final_context_question_no_label', 'paws_labeled_final_paraphrase_task',
            'paws_labeled_final_task_description_no_label', 'piqa_Correct_the_solution',
            'piqa_Correct_the_solution_if_false_from_sol_1', 'piqa_Correct_the_solution_if_false_from_sol_2',
            'piqa_Does_this_solution_make_sense_sol1', 'piqa_Does_this_solution_make_sense_sol2',
            'piqa_choose_the_most_appropriate_solution', 'piqa_finish_sentence_with_correct_choice',
            'piqa_no_prompt_needed', 'piqa_pick_correct_choice_index',
            'piqa_pick_correct_choice_with_choice_given_before_goal', 'piqa_what_is_the_correct_ending',
            'qasc_is_correct_1', 'qasc_is_correct_2', 'qasc_qa_with_combined_facts_1', 'qasc_qa_with_separated_facts_1',
            'qasc_qa_with_separated_facts_2', 'qasc_qa_with_separated_facts_3', 'qasc_qa_with_separated_facts_4',
            'qasc_qa_with_separated_facts_5', 'quail_context_description_question_answer_id',
            'quail_context_description_question_answer_text', 'quail_context_description_question_text',
            'quail_context_question_answer_description_id', 'quail_context_question_answer_description_text',
            'quail_context_question_description_answer_id', 'quail_context_question_description_answer_text',
            'quail_context_question_description_text', 'quail_description_context_question_answer_id',
            'quail_description_context_question_answer_text', 'quail_description_context_question_text',
            'quail_no_prompt_id', 'quail_no_prompt_text', 'quarel_choose_between', 'quarel_do_not_use',
            'quarel_heres_a_story', 'quarel_logic_test', 'quarel_testing_students', 'quartz_answer_question_based_on',
            'quartz_answer_question_below', 'quartz_given_the_fact_answer_the_q', 'quartz_having_read_above_passage',
            'quartz_paragraph_question_plain_concat', 'quartz_read_passage_below_choose',
            'quartz_use_info_from_paragraph_question', 'quartz_use_info_from_question_paragraph',
            'quoref_Answer_Friend_Question', 'quoref_Answer_Question_Given_Context', 'quoref_Answer_Test',
            'quoref_Context_Contains_Answer', 'quoref_Find_Answer', 'quoref_Found_Context_Online',
            'quoref_Given_Context_Answer_Question', 'quoref_Guess_Answer', 'quoref_Guess_Title_For_Context',
            'quoref_Read_And_Extract_', 'quoref_What_Is_The_Answer', 'race_high_Is_this_the_right_answer',
            'race_high_Read_the_article_and_answer_the_question_no_option_', 'race_high_Select_the_best_answer',
            'race_high_Select_the_best_answer_generate_span_', 'race_high_Select_the_best_answer_no_instructions_',
            'race_high_Taking_a_test', 'race_high_Write_a_multi_choice_question_for_the_following_article',
            'race_high_Write_a_multi_choice_question_options_given_', 'race_middle_Is_this_the_right_answer',
            'race_middle_Read_the_article_and_answer_the_question_no_option_', 'race_middle_Select_the_best_answer',
            'race_middle_Select_the_best_answer_generate_span_', 'race_middle_Select_the_best_answer_no_instructions_',
            'race_middle_Taking_a_test', 'race_middle_Write_a_multi_choice_question_for_the_following_article',
            'race_middle_Write_a_multi_choice_question_options_given_', 'ropes_background_new_situation_answer',
            'ropes_background_situation_middle', 'ropes_given_background_situation',
            'ropes_new_situation_background_answer', 'ropes_plain_background_situation', 'ropes_plain_bottom_hint',
            'ropes_plain_no_background', 'ropes_prompt_beginning', 'ropes_prompt_bottom_hint_beginning',
            'ropes_prompt_bottom_no_hint', 'ropes_prompt_mix', 'ropes_read_background_situation',
            'rotten_tomatoes_Movie_Expressed_Sentiment', 'rotten_tomatoes_Movie_Expressed_Sentiment_2',
            'rotten_tomatoes_Reviewer_Enjoyment', 'rotten_tomatoes_Reviewer_Enjoyment_Yes_No',
            'rotten_tomatoes_Reviewer_Expressed_Sentiment', 'rotten_tomatoes_Reviewer_Opinion_bad_good_choices',
            'rotten_tomatoes_Reviewer_Sentiment_Feeling', 'rotten_tomatoes_Sentiment_with_choices_',
            'rotten_tomatoes_Text_Expressed_Sentiment', 'rotten_tomatoes_Writer_Expressed_Sentiment',
            'samsum_Generate_a_summary_for_this_dialogue', 'samsum_Given_the_above_dialogue_write_a_summary',
            'samsum_Sum_up_the_following_dialogue', 'samsum_Summarize_', 'samsum_Summarize_this_dialogue_',
            'samsum_To_sum_up_this_dialog', 'samsum_Write_a_dialogue_that_match_this_summary', 'sciq_Direct_Question',
            'sciq_Direct_Question_Closed_Book_', 'sciq_Multiple_Choice', 'sciq_Multiple_Choice_Closed_Book_',
            'sciq_Multiple_Choice_Question_First', 'social_i_qa_Check_if_a_random_answer_is_valid_or_not',
            'social_i_qa_Generate_answer', 'social_i_qa_Generate_the_question_from_the_answer',
            'social_i_qa_I_was_wondering', 'social_i_qa_Show_choices_and_generate_answer',
            'social_i_qa_Show_choices_and_generate_index', 'squad_v2_Jeopardy_with_Context',
            'squad_v2_Jeopardy_without_Context', 'squad_v2_Questions_with_Context',
            'squad_v2_Questions_with_Context_Without_Prompt_Keywords',
            'squad_v2_Questions_with_Context_Without_Prompt_Keywords_unanswerable',
            'squad_v2_Questions_with_Context_unanswerable', 'squad_v2_Topic_Prediction_Context',
            'squad_v2_Topic_Prediction_Context_with_randomized_prompt_options',
            'squad_v2_Topic_Prediction_Context_with_randomized_prompt_options_placed_in_the_end',
            'squad_v2_Topic_Prediction_Question_and_Answer_Pair', 'squad_v2_Trivia', 'squad_v2_Unanwerable_question',
            'super_glue_boolq_GPT_3_Style', 'super_glue_boolq_I_wonder_', 'super_glue_boolq_after_reading',
            'super_glue_boolq_based_on_the_following_passage', 'super_glue_boolq_based_on_the_previous_passage',
            'super_glue_boolq_could_you_tell_me_', 'super_glue_boolq_exam', 'super_glue_boolq_exercise',
            'super_glue_boolq_valid_binary', 'super_glue_boolq_yes_no_question', 'super_glue_cb_GPT_3_style',
            'super_glue_cb_GPT_3_style_score_eval', 'super_glue_cb_MNLI_crowdsource',
            'super_glue_cb_MNLI_crowdsource_score_eval', 'super_glue_cb_always_sometimes_never',
            'super_glue_cb_always_sometimes_never_score_eval', 'super_glue_cb_based_on_the_previous_passage',
            'super_glue_cb_based_on_the_previous_passage_score_eval', 'super_glue_cb_can_we_infer',
            'super_glue_cb_can_we_infer_score_eval', 'super_glue_cb_claim_true_false_inconclusive',
            'super_glue_cb_claim_true_false_inconclusive_score_eval', 'super_glue_cb_consider_always_sometimes_never',
            'super_glue_cb_consider_always_sometimes_never_score_eval', 'super_glue_cb_does_it_follow_that',
            'super_glue_cb_does_it_follow_that_score_eval', 'super_glue_cb_does_this_imply',
            'super_glue_cb_does_this_imply_score_eval', 'super_glue_cb_guaranteed_possible_impossible',
            'super_glue_cb_guaranteed_possible_impossible_score_eval', 'super_glue_cb_guaranteed_true',
            'super_glue_cb_guaranteed_true_score_eval', 'super_glue_cb_justified_in_saying',
            'super_glue_cb_justified_in_saying_score_eval', 'super_glue_cb_must_be_true',
            'super_glue_cb_must_be_true_score_eval', 'super_glue_cb_should_assume',
            'super_glue_cb_should_assume_score_eval', 'super_glue_cb_take_the_following_as_truth',
            'super_glue_cb_take_the_following_as_truth_score_eval', 'super_glue_copa_C1_or_C2_premise_so_because_',
            'super_glue_copa_C1_or_C2_premise_so_because__score_eval', 'super_glue_copa__As_a_result_C1_or_C2_',
            'super_glue_copa__As_a_result_C1_or_C2__score_eval', 'super_glue_copa__What_could_happen_next_C1_or_C2_',
            'super_glue_copa__What_could_happen_next_C1_or_C2__score_eval', 'super_glue_copa__which_may_be_caused_by',
            'super_glue_copa__which_may_be_caused_by_score_eval', 'super_glue_copa__why_C1_or_C2',
            'super_glue_copa__why_C1_or_C2_score_eval', 'super_glue_copa_best_option',
            'super_glue_copa_best_option_score_eval', 'super_glue_copa_cause_effect',
            'super_glue_copa_cause_effect_score_eval', 'super_glue_copa_choose', 'super_glue_copa_choose_score_eval',
            'super_glue_copa_exercise', 'super_glue_copa_exercise_score_eval', 'super_glue_copa_i_am_hesitating',
            'super_glue_copa_i_am_hesitating_score_eval', 'super_glue_copa_more_likely',
            'super_glue_copa_more_likely_score_eval', 'super_glue_copa_plausible_alternatives',
            'super_glue_copa_plausible_alternatives_score_eval', 'super_glue_multirc_I_was_going_to_say_',
            'super_glue_multirc_Would_it_be_good_to_answer_', 'super_glue_multirc_confirm',
            'super_glue_multirc_correct', 'super_glue_multirc_decide_valid', 'super_glue_multirc_found_this_answer',
            'super_glue_multirc_grading', 'super_glue_multirc_is_a_correct_answer_',
            'super_glue_multirc_is_the_correct_answer_', 'super_glue_multirc_paragraph_question_is_it_',
            'super_glue_record_Add_sentence_after_after_continuation_choices_',
            'super_glue_record_Add_sentence_after_continuation_choices_', 'super_glue_record_Can_you_figure_out_',
            'super_glue_record_GPT_3_style_continuation_choices_',
            'super_glue_record_GPT_3_style_summary_only_continuation_choices_',
            'super_glue_record_GPT_3_style_with_labels_continuation_choices_',
            'super_glue_record_GPT_3_style_with_labels_without_hyphens_continuation_choices_',
            'super_glue_record_GPT_3_style_without_hyphens_continuation_choices_',
            'super_glue_record_In_the_question_above_the_placeholder_stands_for',
            'super_glue_record_New_highlight_continuation_choices_',
            'super_glue_record_News_article_continuation_choices_',
            'super_glue_record_Summary_first_continuation_choices_', 'super_glue_record_What_could_the_placeholder_be_',
            'super_glue_record_Which_one_is_the_placeholder_', 'super_glue_record_choose_between',
            'super_glue_record_corrupted', 'super_glue_record_exercise', 'super_glue_record_pick_one_option',
            'super_glue_record_the_placeholder_refers_to_', 'super_glue_record_trying_to_decide',
            'super_glue_rte_GPT_3_style', 'super_glue_rte_GPT_3_style_score_eval', 'super_glue_rte_MNLI_crowdsource',
            'super_glue_rte_MNLI_crowdsource_score_eval', 'super_glue_rte_based_on_the_previous_passage',
            'super_glue_rte_based_on_the_previous_passage_score_eval', 'super_glue_rte_can_we_infer',
            'super_glue_rte_can_we_infer_score_eval', 'super_glue_rte_does_it_follow_that',
            'super_glue_rte_does_it_follow_that_score_eval', 'super_glue_rte_does_this_imply',
            'super_glue_rte_does_this_imply_score_eval', 'super_glue_rte_guaranteed_true',
            'super_glue_rte_guaranteed_true_score_eval', 'super_glue_rte_justified_in_saying',
            'super_glue_rte_justified_in_saying_score_eval', 'super_glue_rte_must_be_true',
            'super_glue_rte_must_be_true_score_eval', 'super_glue_rte_should_assume',
            'super_glue_rte_should_assume_score_eval', 'super_glue_wic_GPT_3_prompt',
            'super_glue_wic_GPT_3_prompt_score_eval', 'super_glue_wic_GPT_3_prompt_with_label',
            'super_glue_wic_GPT_3_prompt_with_label_score_eval', 'super_glue_wic_affirmation_true_or_false',
            'super_glue_wic_affirmation_true_or_false_score_eval', 'super_glue_wic_grammar_homework',
            'super_glue_wic_grammar_homework_score_eval', 'super_glue_wic_polysemous',
            'super_glue_wic_polysemous_score_eval', 'super_glue_wic_question_context',
            'super_glue_wic_question_context_meaning', 'super_glue_wic_question_context_meaning_score_eval',
            'super_glue_wic_question_context_meaning_with_label',
            'super_glue_wic_question_context_meaning_with_label_score_eval',
            'super_glue_wic_question_context_score_eval', 'super_glue_wic_same_sense',
            'super_glue_wic_same_sense_score_eval', 'super_glue_wic_similar_sense',
            'super_glue_wic_similar_sense_score_eval', 'super_glue_wsc.fixed_GPT_3_Style',
            'super_glue_wsc.fixed_GPT_3_Style_score_eval', 'super_glue_wsc.fixed_I_think_they_mean',
            'super_glue_wsc.fixed_I_think_they_mean_score_eval', 'super_glue_wsc.fixed_Who_or_what_is_are',
            'super_glue_wsc.fixed_Who_or_what_is_are_score_eval', 'super_glue_wsc.fixed_by_p_they_mean',
            'super_glue_wsc.fixed_by_p_they_mean_score_eval', 'super_glue_wsc.fixed_does_p_stand_for',
            'super_glue_wsc.fixed_does_p_stand_for_score_eval', 'super_glue_wsc.fixed_does_the_pronoun_refer_to',
            'super_glue_wsc.fixed_does_the_pronoun_refer_to_score_eval', 'super_glue_wsc.fixed_in_other_words',
            'super_glue_wsc.fixed_in_other_words_score_eval', 'super_glue_wsc.fixed_p_is_are_r',
            'super_glue_wsc.fixed_p_is_are_r_score_eval', 'super_glue_wsc.fixed_replaced_with',
            'super_glue_wsc.fixed_replaced_with_score_eval', 'super_glue_wsc.fixed_the_pronoun_refers_to',
            'super_glue_wsc.fixed_the_pronoun_refers_to_score_eval', 'trec_fine_grained_ABBR',
            'trec_fine_grained_ABBR_context_first', 'trec_fine_grained_DESC', 'trec_fine_grained_DESC_context_first',
            'trec_fine_grained_ENTY', 'trec_fine_grained_HUM', 'trec_fine_grained_HUM_context_first',
            'trec_fine_grained_LOC', 'trec_fine_grained_LOC_context_first', 'trec_fine_grained_NUM',
            'trec_fine_grained_NUM_context_first', 'trec_fine_grained_open', 'trec_fine_grained_open_context_first',
            'trec_pick_the_best_descriptor', 'trec_trec1', 'trec_trec2', 'trec_what_category_best_describe',
            'trec_which_category_best_describes', 'trivia_qa_unfiltered_first_person_context',
            'trivia_qa_unfiltered_formal_description', 'trivia_qa_unfiltered_guess_question',
            'trivia_qa_unfiltered_question_answer', 'trivia_qa_unfiltered_question_with_instruction',
            'web_questions_get_the_answer', 'web_questions_potential_correct_answer', 'web_questions_question_answer',
            'web_questions_short_general_knowledge_q', 'web_questions_whats_the_answer', 'wiki_bio_comprehension',
            'wiki_bio_guess_person', 'wiki_bio_key_content', 'wiki_bio_what_content', 'wiki_bio_who',
            'wiki_hop_original_choose_best_object_affirmative_1', 'wiki_hop_original_choose_best_object_affirmative_2',
            'wiki_hop_original_choose_best_object_affirmative_3',
            'wiki_hop_original_choose_best_object_interrogative_1',
            'wiki_hop_original_choose_best_object_interrogative_2', 'wiki_hop_original_explain_relation',
            'wiki_hop_original_generate_object', 'wiki_hop_original_generate_subject',
            'wiki_hop_original_generate_subject_and_object', 'wiki_qa_Decide_good_answer',
            'wiki_qa_Direct_Answer_to_Question', 'wiki_qa_Generate_Question_from_Topic', 'wiki_qa_Is_This_True_',
            'wiki_qa_Jeopardy_style', 'wiki_qa_Topic_Prediction_Answer_Only', 'wiki_qa_Topic_Prediction_Question_Only',
            'wiki_qa_Topic_Prediction_Question_and_Answer_Pair', 'wiki_qa_automatic_system', 'wiki_qa_exercise',
            'wiki_qa_found_on_google', 'winogrande_winogrande_debiased_Replace',
            'winogrande_winogrande_debiased_Replace_score_eval',
            'winogrande_winogrande_debiased_does_underscore_refer_to',
            'winogrande_winogrande_debiased_does_underscore_refer_to_score_eval',
            'winogrande_winogrande_debiased_fill_in_the_blank',
            'winogrande_winogrande_debiased_fill_in_the_blank_score_eval', 'winogrande_winogrande_debiased_stand_for',
            'winogrande_winogrande_debiased_stand_for_score_eval', 'winogrande_winogrande_debiased_underscore_refer_to',
            'winogrande_winogrande_debiased_underscore_refer_to_score_eval', 'winogrande_winogrande_xl_Replace',
            'winogrande_winogrande_xl_Replace_score_eval', 'winogrande_winogrande_xl_does_underscore_refer_to',
            'winogrande_winogrande_xl_does_underscore_refer_to_score_eval',
            'winogrande_winogrande_xl_fill_in_the_blank', 'winogrande_winogrande_xl_fill_in_the_blank_score_eval',
            'winogrande_winogrande_xl_stand_for', 'winogrande_winogrande_xl_stand_for_score_eval',
            'winogrande_winogrande_xl_underscore_refer_to', 'winogrande_winogrande_xl_underscore_refer_to_score_eval',
            'wiqa_does_the_supposed_perturbation_have_an_effect', 'wiqa_effect_with_label_answer',
            'wiqa_effect_with_string_answer', 'wiqa_what_is_the_final_step_of_the_following_process',
            'wiqa_what_is_the_missing_first_step', 'wiqa_what_might_be_the_first_step_of_the_process',
            'wiqa_what_might_be_the_last_step_of_the_process',
            'wiqa_which_of_the_following_is_the_supposed_perturbation', 'xsum_DOC_boils_down_to_simple_idea_that',
            'xsum_DOC_given_above_write_one_sentence', 'xsum_DOC_how_would_you_rephrase_few_words', 'xsum_DOC_tldr',
            'xsum_DOC_write_summary_of_above', 'xsum_article_DOC_summary', 'xsum_college_roommate_asked_DOC_so_I_recap',
            'xsum_read_below_DOC_write_abstract', 'xsum_summarize_DOC', 'xsum_summarize_this_DOC_summary',
            'yelp_review_full_based_on_that', 'yelp_review_full_format_rating', 'yelp_review_full_format_score',
            'yelp_review_full_format_star', 'yelp_review_full_on_a_scale', 'yelp_review_full_so_i_would',
            'yelp_review_full_this_place']

data_name = "yelp_review_full_this_place"

dataset = load_dataset(path="bigscience/P3", name=data_name, cache_dir='./p3_data')
dataset.save_to_disk('p3_data_adversarial_qa_dbert_based_on')
print("保存成功：{}".format(data_name))

# from datasets import load_dataset
# dataset = load_dataset('super_glue', 'cb', cache_dir='./raw_datasets')
# dataset.save_to_disk('super_glue_cb')