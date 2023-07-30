def get_file_names() -> (str, str, str):
    rule_file_name = input("규칙이 저장된 엑셀 파일 이름을 입력해 주세요. (확장자는 입력 X)\n > ")
    original_file_name = input("\n비용 현황이 저장된 파일 이름을 입력해 주세요. (확장자는 입력 X)\n > ")

    output_file_name = f"output_{original_file_name}"
    print(f"\n결과 출력 파일명 > {output_file_name}.xlsx")

    return rule_file_name, original_file_name, output_file_name
