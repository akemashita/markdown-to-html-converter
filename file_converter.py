import sys
import os
import markdown


def main():
    if len(sys.argv) != 4 or sys.argv[1] != 'markdown':
        show_usage()
        sys.exit(1)

    # script_name = sys.argv[0]
    # command = sys.argv[1]
    input_filepath = sys.argv[2]
    output_filepath = check_output_filepath(sys.argv[3])

    try:
        # with open(input_filepath, 'r', encoding='utf-8') as input_f:
        #     input_data = input_f.read()
        # html = markdown.markdown(input_data, extensions=['tables'])

        # with open(output_filepath, 'w', encoding='utf-8') as output_f:
        #     output_f.write(html)

        markdown.markdownFromFile(input=input_filepath, output=output_filepath, extensions=['tables'])
        print(f'処理が正常に完了しました。出力ファイルパス：{output_filepath}')

    except FileNotFoundError:
        print(f'無効な入力ファイルパスです。{input_filepath} が存在しません。')

    except Exception as e:
        print(f'エラーが発生しました:：{e}')


def show_usage():
    print('入力に誤りがあります。次の例を参考に入力してください。')
    print('python3 file_converter.py markdown <input_filepath> <output_filepath>')


def check_output_filepath(output_filepath):
    try:
        with open(output_filepath, 'w') as f:
            f.write('create for testing.')

        os.remove(output_filepath)
        return output_filepath

    except:
        return 'output.html' # エラーが発生した場合は同じフォルダに output.html で出力する



if __name__ == '__main__':
    main()
