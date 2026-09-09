CREATE TABLE taskdetails (
    task_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_name VARCHAR(255) NOT NULL,
    task_description TEXT,
    task_deadline TIMESTAMP WITH TIME ZONE,
    task_status VARCHAR(50) NOT NULL DEFAULT 'pending',
    task_comment TEXT,
    task_assign VARCHAR(255),
    task_created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    task_updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

select * from taskdetails