fetch_lesson_progress_query = """query fetch_lesson_progress ($session_id: String!, $student_key: String!) {
    fetch_lesson_progress (session_id: $session_id, student_key: $student_key) {
        id
        title
        key
        version
        locale
        aggregated_state {
            completion_amount
        }
        parts {
            id
            title
            aggregated_state {
                completion_amount
            }
            modules {
                lessons {
                    id
                    title
                    aggregated_state {
                        completion_amount
                    }
                }
            }
        }
    }
}"""
