import os

from dotenv import load_dotenv


load_dotenv()


def _env(name, default):
    return os.getenv(name, default)


def _int_env(name, default):
    return int(os.getenv(name, str(default)))


# 실제 테스트 실행 시 .env에 실제 교실/강의/자료 ID를 넣어야 합니다.
lecture_case = {
    "lecture_material_type": "3",
    "lecture_quiz_material_type": "5",
    "lecture_exercise_material_type": "4",

    "week1_course_id": _env("week1_course_id", "111111"),
    "week1_course_section_id": _env("week1_course_section_id", "1111111"),

    "week1_2lecture_id": _env("week1_2lecture_id", "2222222"),
    "week1_2lecture_page_id": _env("week1_2lecture_page_id", "33333333"),
    "week1_2lecture_material_id": _env(
        "week1_2lecture_material_id", "33333333"),

    "week1_2lecture_1quiz_page_id": _env(
        "week1_2lecture_1quiz_page_id", "33333334"),
    "week1_2lecture_1quiz_material_id": _env(
        "week1_2lecture_1quiz_material_id", "33333334"),

    "week1_2lecture_1exercise_page_id": _env(
        "week1_2lecture_1exercise_page_id", "33333335"),
    "week1_2lecture_1exercise_material_id": _env(
        "week1_2lecture_1exercise_material_id", "33333335"),
    "week1_2lecture_1exercise_room_id": _env(
        "week1_2lecture_1exercise_room_id", "44444444"),

    "submit_exercise_material_id": _env(
        "submit_exercise_material_id", "33333336"),
    "submit_exercise_room_id": _env("submit_exercise_room_id", "44444445"),


}

teacher_course_case = {
    "lecture_page_id": _int_env("teacher_lecture_page_id", 55555555),
    "course_id": _int_env("teacher_course_id", 666666),
    "lecture_id": _int_env("teacher_lecture_id", 7777777),
    "add_course_id": _int_env("teacher_add_course_id", 666667),
    "material_quiz_id": _int_env("teacher_material_quiz_id", 55555556),
    "pdf_lecture_page_id": _int_env(
        "teacher_pdf_lecture_page_id", 55555557),
    "pdf_lecture_id": _int_env("teacher_pdf_lecture_id", 7777778),
    "pdf_material_id": _int_env("teacher_pdf_material_id", 55555557),
}
