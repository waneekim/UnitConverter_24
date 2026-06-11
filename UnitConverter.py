from convert_length import convert_length
from length_spec import LengthSpecError

INPUT_PROMPT = "Insert value for converting (ex: meter:2.5): "


def process_input(input_str: str) -> tuple[list[str], str | None]:
    """stdin 한 줄을 파싱·변환. (출력 줄 목록, 오류 메시지) — 오류 시 줄 목록은 []."""
    try:
        result = convert_length(input_str.strip())
    except LengthSpecError as e:
        return [], str(e)

    lines = [
        f"{result.input_spec} = {result.meter} meter",
        f"{result.input_spec} = {result.feet} feet",
        f"{result.input_spec} = {result.yard} yard",
    ]
    return lines, None


def main() -> None:
    input_str = input(INPUT_PROMPT)
    lines, error = process_input(input_str)
    if error:
        print(error)
        return
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
