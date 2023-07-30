def get_file_names() -> (str, str, str):
    rule_file_name = "rules"
    original_file_name = input("\n비용 현황이 저장된 파일 이름을 입력해 주세요. (확장자 생략 가능)\n > ")

    if "." in original_file_name:
        original_file_name = original_file_name.split(".")[0]

    output_file_name = f"output_{original_file_name}"
    print(f"\n결과 파일은 {output_file_name}.xlsx 에 저장돼요.")

    return rule_file_name, original_file_name, output_file_name
