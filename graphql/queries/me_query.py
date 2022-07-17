me_query = """query me {
    me {
        id
        personal_info {
            email
            first_name
            last_name
            nickname
        }
        roles {
            admin
            facilitator
            student
        }
        enrollments {
            type
            session_type
            id
            r2_enrollment_id
            student_key
            session_id
            degree_id
            active
            created_at
            updated_at
            unenrolled_at
            unenrollment_reason
            status
            nanodegree_status
            graduated_at
            should_force_ratings
        }
        session {
            id
            name
            num_enrolled
            max_attendees
            active
            canceled_at
            full_time
            type
            cohort_id
            degree {
                id
                version
                locale
            }
            meeting_days {
                timezone
                day_index
                start_time
                end_time
            }
            location {
                type
                id
                name
                instructions
            }
            location_id
            facilitator {
                id
                name
                title
                bio
                image_url
                role
            }
            facilitators {
                id
                name
                title
                bio
                image_url
                role
            }
            instances {
                id
                session_id
                start
                end
                door_code
            }
            customer_type
            is_test_session
            hide_from_classroom
            deadlines {
                type
                due_datetime
            }
            members {
                student {
                    key
                    email
                    first_name
                    last_name
                    nickname
                }
                enrollment {
                    type
                    session_type
                    id
                    r2_enrollment_id
                    student_key
                    session_id
                    degree_id
                    active
                    created_at
                    updated_at
                    unenrolled_at
                    unenrollment_reason
                    status
                    nanodegree_status
                    graduated_at
                    should_force_ratings
                }
                attendances {
                    id
                    student_key
                    status
                    instance_id
                    instance_start_datetime
                }
            }
            partners {
                id
                name
                logo_url
                country
                created_at
                updated_at
            }
            created_at
            updated_at
        }
        sessions {
            id
            name
            num_enrolled
            max_attendees
            active
            canceled_at
            full_time
            type
            cohort_id
            degree {
                id
                version
                locale
            }
            meeting_days {
                timezone
                day_index
                start_time
                end_time
            }
            location {
                type
                id
                name
                instructions
            }
            location_id
            facilitator {
                id
                name
                title
                bio
                image_url
                role
            }
            facilitators {
                id
                name
                title
                bio
                image_url
                role
            }
            instances {
                id
                session_id
                start
                end
                door_code
            }
            customer_type
            is_test_session
            hide_from_classroom
            deadlines {
                type
                due_datetime
            }
            members {
                student {
                    key
                    email
                    first_name
                    last_name
                    nickname
                }
                enrollment {
                    type
                    session_type
                    id
                    r2_enrollment_id
                    student_key
                    session_id
                    degree_id
                    active
                    created_at
                    updated_at
                    unenrolled_at
                    unenrollment_reason
                    status
                    nanodegree_status
                    graduated_at
                    should_force_ratings
                }
                attendances {
                    id
                    student_key
                    status
                    instance_id
                    instance_start_datetime
                }
            }
            partners {
                id
                name
                logo_url
                country
                created_at
                updated_at
            }
            created_at
            updated_at
        }
        ratings {
            id
            instance {
                id
                session_id
                start
                end
                door_code
            }
            facilitator {
                id
                name
                title
                bio
                image_url
                role
            }
            student_key
            session_id
            value
            comments
            created_at
        }
        attendances {
            id
            student_key
            status
            instance_id
            instance_start_datetime
        }
    }
}"""
