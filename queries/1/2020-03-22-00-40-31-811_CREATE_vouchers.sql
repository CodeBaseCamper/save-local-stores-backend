CREATE TABLE "public"."vouchers" (
   "id" serial4,
   "shop_id" int4 NOT NULL,
   "timestamp" date NOT NULL DEFAULT NOW(),
   "amount" varchar(255) NOT NULL,
   "code" text NOT NULL,
   PRIMARY KEY ("id")
 );
