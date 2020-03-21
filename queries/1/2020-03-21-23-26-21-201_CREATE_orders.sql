CREATE TABLE "public"."orders" (
   "id" serial4,
   "shop_id" int4 NOT NULL,
   "user_email" varchar(255) NOT NULL,
   "voucher" text NOT NULL,
   PRIMARY KEY ("id"),
   FOREIGN KEY ("shop_id") REFERENCES "public"."shops" ("id") ON DELETE CASCADE ON UPDATE NO ACTION,
   UNIQUE ("voucher")
 );
