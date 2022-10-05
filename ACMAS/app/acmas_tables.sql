create table "ACMAS_Web_university"
(
    id   bigserial
        primary key,
    name varchar(50) not null
);

alter table "ACMAS_Web_university"
    owner to hello_acmas;

create table "ACMAS_Web_course"
(
    id         bigserial
        primary key,
    name       text        not null,
    code       varchar(20) not null,
    university text        not null,
    semster    varchar(30) not null,
    years      text        not null,
    test_type  varchar(20) not null
);

alter table "ACMAS_Web_course"
    owner to hello_acmas;


create table "ACMAS_Web_question"
(
    id        bigserial
        primary key,
    filename  text not null,
    question  text not null,
    "Answers" text not null,
    "Hash"    text not null
);

alter table "ACMAS_Web_question"
    owner to hello_acmas;


create table "ACMAS_Web_uploadedfile"
(
    id            bigserial
        primary key,
    filename      varchar(60) not null,
    file_dir      text        not null,
    date_uploaded varchar(50) not null,
    flag          varchar(80) not null,
    course_id     bigint      not null
        constraint "ACMAS_Web_uploadedfi_Course_id_0d560cf7_fk_ACMAS_Web"
            references "ACMAS_Web_course"
            deferrable initially deferred
);

alter table "ACMAS_Web_uploadedfile"
    owner to hello_acmas;

create index "ACMAS_Web_uploadedfile_Course_id_0d560cf7"
    on "ACMAS_Web_uploadedfile" (course_id);

