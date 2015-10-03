class CreateLocations < ActiveRecord::Migration
  def change
    create_table :locations do |t|
      t.string :city
      t.string :country
      t.string :scholarship
      t.string :contest
      t.string :extracurricular

      t.timestamps null: false
    end
  end
end
