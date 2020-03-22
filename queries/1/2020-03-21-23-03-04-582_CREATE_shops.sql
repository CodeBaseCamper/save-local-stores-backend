CREATE TABLE "public"."shops" (
   "id" serial4,
   "name" varchar(255) NOT NULL,
   "description" text NOT NULL,
   "owner_firstname" varchar(255) NOT NULL,
   "owner_lastname" varchar(255) NOT NULL,
   "street" varchar(255) NOT NULL,
   "street_number" varchar(255) NOT NULL,
   "zip_code" varchar(255) NOT NULL,
   "picture" int4,
   "owner_picture" int4,
   "business_categorie_id" int4 NOT NULL,
   PRIMARY KEY ("id"),
   FOREIGN KEY ("business_categorie_id") REFERENCES "public"."business_categories" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
 );
