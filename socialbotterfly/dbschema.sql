-- Tasks are steps that can be taken to complete a project
create table user_data (
    nickname          text primary key unique not null,
    latitude          float,
    longitude         float,
    max_distance_km   float,
    unsubscribed      bool default false,
    banned            bool default false,
    favourite_things  text,
    blacklist_things  text,
    last_suggestion   date,
    already_suggested text
);
