import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from constants import DEFAULT_ESTIMATE_DECIMAL_PLACES
from convert_length import convert_length, convert_lengths
from length_spec import LengthSpecError

INPUT_PROMPT = '변환할 치수를 입력하세요 (예: meter:2.5 또는 3\'-6"): '
BATCH_PROMPT = "치수를 한 줄씩 입력하세요 (빈 줄이면 변환 시작): "
ERROR_INVALID_FORMAT = '형식이 올바르지 않습니다. 예: meter:2.5 또는 3\'-6"'
ERROR_UNKNOWN_UNIT = "알 수 없는 단위: {unit}. 예: meter, feet, yard"


def _format_length_spec_error(exc: LengthSpecError) -> str:
    msg = str(exc)
    if msg.startswith("Unknown unit:"):
        unit = msg.split(":", 1)[1].strip()
        return ERROR_UNKNOWN_UNIT.format(unit=unit)
    if (
        "Invalid format" in msg
        or "Invalid arch" in msg
        or "Invalid fraction" in msg
    ):
        return ERROR_INVALID_FORMAT
    return msg


def _format_result_lines(result) -> list[str]:
    places = DEFAULT_ESTIMATE_DECIMAL_PLACES
    meter = round(result.meter, places)
    feet = (
        result.estimate_rounded
        if result.estimate_rounded is not None
        else round(result.feet, places)
    )
    yard = round(result.yard, places)
    return [
        f"{result.input_spec} = {meter} meter",
        f"{result.input_spec} = {feet} feet",
        f"{result.input_spec} = {yard} yard",
    ]


def process_input(input_str: str) -> tuple[list[str], str | None]:
    """stdin 한 줄을 파싱·변환. (출력 줄 목록, 오류 메시지) — 오류 시 줄 목록은 []."""
    try:
        result = convert_length(input_str.strip())
    except LengthSpecError as e:
        return [], _format_length_spec_error(e)

    return _format_result_lines(result), None


def process_batch_input(specs: list[str]) -> tuple[list[str], str | None]:
    """N치수 일괄 변환 — convert_lengths 위임, boundary I/O 조립만."""
    stripped = [s.strip() for s in specs if s.strip()]
    if not stripped:
        return [], None
    try:
        results = convert_lengths(stripped)
    except LengthSpecError as e:
        return [], _format_length_spec_error(e)
    all_lines: list[str] = []
    for result in results:
        all_lines.extend(_format_result_lines(result))
    return all_lines, None


def main() -> None:
    print(INPUT_PROMPT)
    print("(여러 치수: 한 줄씩 입력 후 빈 줄)")
    specs: list[str] = []
    while True:
        line = input(BATCH_PROMPT).strip()
        if not line:
            break
        specs.append(line)

    if not specs:
        line = input("치수 1개: ").strip()
        if line:
            specs = [line]

    if not specs:
        return

    if len(specs) == 1:
        lines, error = process_input(specs[0])
    else:
        lines, error = process_batch_input(specs)

    if error:
        print(error)
        return
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
