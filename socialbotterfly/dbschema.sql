-- Tasks are steps that can be taken to complete a project
create table user_data (
    nickname          text primary key unique not null,
    latitude          float,
    longitude         float,
    zone_id           integer,
    min_distance_km   float,
    max_distance_km   float,
    unsubscribed      bool default false,
    banned            bool default false,
    favourite_things  text,
    blacklist_things  text,
    suggestion_freq   text,
    communities       text,
    last_suggestion   date,
    already_suggested text
);
