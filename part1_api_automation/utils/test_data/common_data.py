import os

from dotenv import load_dotenv


load_dotenv()


def _env(name, default):
    return os.getenv(name, default)


base_rest_url = "https://api-rest.elice.io"

base_classroom_url = "https://api-classroom.elice.io"

base_dashboard_url = "https://api-dashboard.elice.io"

base_course_url = "https://api-course.elice.io"

base_org_url = "https://api-org.elice.io"

base_account_url = "https://api-account.elice.io"

base_community_url = "https://api-community.elice.io"

base_file_url = "https://api-file.elice.io"

base_notification_url = "https://api-notification.elice.io"

base_billing2_url = "https://api-billing2.elice.io"

base_channel_url = "https://api-channel.elice.io"

# 실제 테스트 실행 시 .env에 실제 조직명과 교실 ID를 넣어야 합니다.
org_student = _env("org_student", "sample-student-org")

org_teacher = _env("org_teacher", "sample-teacher-org")

student_classroom_id = _env(
    "student_classroom_id", "00000000-0000-0000-0000-000000000001")

teacher_classroom_id = _env(
    "teacher_classroom_id", "00000000-0000-0000-0000-000000000002")

file_resource_id = _env(
    "file_resource_id", "00000000-0000-0000-0000-000000000003")


# 운영 서비스 보호를 위한 API 요청 최소 간격
min_request_interval_seconds = 0.3
