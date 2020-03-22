ALTER TABLE "public"."orders" 
   DROP COLUMN "shop_id",
   DROP COLUMN "timestamp",
   ALTER COLUMN "voucher_id" TYPE int4 USING "voucher_id"::int4,
   ADD FOREIGN KEY ("voucher_id") REFERENCES "public"."vouchers" ("id") ON DELETE CASCADE ON UPDATE NO ACTION
