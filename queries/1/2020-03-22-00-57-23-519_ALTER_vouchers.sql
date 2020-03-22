ALTER TABLE "public"."vouchers" 
   ALTER COLUMN "timestamp" TYPE timestamp(0) USING "timestamp"::timestamp(0)
