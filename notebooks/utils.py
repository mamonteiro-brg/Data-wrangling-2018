import pandas as pd


def clean_api_df(df,drop_columns=None):
	df = df.copy()
	if drop_columns is None:
		return df
	else:
		return df.drop(columns=drop_columns)


def join_target_api(target_df,api_df):
	return target_df.join(api_df)

def join_to_sql(target_df,api_df):
	return target_df.join(api_df)		

def prepare_dataset(df):
	df = df.copy()
	drop_columns = ['DEF_60_CNT_SOCIAL_CIRCLE','BASEMENTAREA_AVG','ENTRANCES_AVG','FONDKAPREMONT_MODE','OWN_CAR_AGE','name_education_type','name_income_type']
	df = df.drop(columns=drop_columns)
	df['flag_document_9'] = df.flag_document_9.astype('int')
	df['flag_document_13'] = df.flag_document_13.astype('int')
	return df