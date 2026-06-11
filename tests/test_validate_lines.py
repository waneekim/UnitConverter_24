from validate_lines import validate_lines

ARCH_3FT_6IN = '3\'-6"'
ARCH_9FT_2IN = '9\'-2"'

# Mom Test 철골 치수 8개 fixture (session-workbook 성공 기준 3)
STEEL_DIMS_8 = [
    [ARCH_3FT_6IN],
    [ARCH_9FT_2IN],
    ['12\'-0"'],
    ['6\'-8"'],
    ['4\'-0"'],
    ['10\'-6"'],
    ['8\'-3"'],
    ['5\'-4"'],
]


def test_arch_notation_3ft_6in_passes():
    # Arrange — R1: 3'-6" = 3.75 feet (Mom Test 15분 손실 케이스의 정답 표기)
    grid = [[ARCH_3FT_6IN]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_feet_3_5_misrepresents_3ft_6in_fails():
    # Arrange — R1: feet:3.5는 3'-6"(3.75) 오환산 (Mom Test 증거 #1)
    grid = [[ARCH_3FT_6IN, "feet:3.5"]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]


def test_feet_and_yard_same_value_is_confusion():
    # Arrange — R2: 야드·피트 동일 수치 = 단위 혼동 (Mom Test 3만 원 손실)
    grid = [["feet:3", "yard:3"]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]


def test_meter_feet_yard_inconsistent_fails():
    # Arrange — R2: meter 기준 feet↔yard 비율 불일치
    grid = [["meter:1.0", "feet:3.28084", "yard:1.0"]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]


def test_unknown_unit_fails_with_line_index():
    # Arrange — R4: 알 수 없는 단위
    grid = [["foo:1.0"]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert 0 in result["failed_lines"]


def test_missing_colon_fails():
    # Arrange — R4: 콜론 누락 (Mom Test 2분 손실)
    grid = [["meter2.5"]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]


def test_empty_cell_marks_incomplete():
    # Arrange — R4: 빈 셀 = 미완 입력
    grid = [[ARCH_3FT_6IN, ""]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []


def test_eight_steel_dims_all_pass():
    # Arrange — 성공 기준 3: 8개 철골 치수 일괄 pass (Mom Test 10분 손실 대안)
    grid = STEEL_DIMS_8
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_eight_steel_dims_one_misconversion_fails():
    # Arrange — 성공 기준 3 Red: 8개 중 1개 오환산 → fail + 행 인덱스
    grid = [
        [ARCH_3FT_6IN],
        [ARCH_9FT_2IN],
        ['12\'-0"'],
        ['6\'-8"'],
        ["feet:3.5"],  # row 4: 3'-6"을 3.5로 오입력한 유형
        ['10\'-6"'],
        ['8\'-3"'],
        ['5\'-4"'],
    ]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [4]
