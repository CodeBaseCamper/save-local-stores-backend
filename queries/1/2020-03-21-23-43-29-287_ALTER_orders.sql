ALTER TABLE "public"."orders" 
   ADD COLUMN "timestamp" time NOT NULL DEFAULT NOW()
