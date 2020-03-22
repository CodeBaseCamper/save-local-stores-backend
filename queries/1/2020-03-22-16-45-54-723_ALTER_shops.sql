ALTER TABLE "public"."shops" 
   ADD FOREIGN KEY ("owner_picture") REFERENCES "public"."images" ("id") ON DELETE CASCADE ON UPDATE NO ACTION
