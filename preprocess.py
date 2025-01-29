import pandas as pd


def load_all_files(directory_path=r'C:\Users\12574\PycharmProjects\BeihangProgrammingC\dataset\C2022',
                   extention='xlsx'):
    import os
    import glob

    target_files = glob.glob(os.path.join(directory_path, '**/*.' + extention), recursive=True)

    return target_files


def parse_xlsx(file_path):
    columns = ['user_id', 'user_name', 'submission_id', 'judge_result','judge_info', 'score', 'language', 'code_lines',
               'execution_time','execution_memory', 'submission_time', 'code']
    try:
        df = pd.read_excel(file_path)

        if len(df.columns) == 12:
            # got what we want
            # modify the index name to english then return
            print(df.columns)
            df.columns = columns
            return df
    # todo: revisit the zip file
    except Exception as e:
        print(e)


def preprocess():
    xlsx_files = load_all_files()

    print(xlsx_files)

    import os
    ret = None
    for file in xlsx_files:
        split = file.split(os.path.sep)
        file_paths, file_name = split[:-1], split[-1]
        problem_name = file_name.split('.')[0]
        df = parse_xlsx(file)
        if df is not  None:
            problem_set = file_paths[-1]
            print(problem_set)
            df['problem_set'] = problem_set
            df['problem_name'] = problem_set + '_' + problem_name
            if ret is None:
                ret = df

            else:
                ret = pd.concat([ret,df])


    ret.to_csv(r'C:\Users\12574\PycharmProjects\BeihangProgrammingC\dataset\C2022\total.csv')




if __name__ == '__main__':
    preprocess()
