ALTER TABLE "public"."shops" 
   ADD COLUMN "city_id" int4 NOT NULL,
   ADD FOREIGN KEY ("city_id") REFERENCES "public"."cities" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
