json.array!(@locations) do |location|
  json.extract! location, :id, :city, :country, :scholarship, :contest, :extracurricular
  json.url location_url(location, format: :json)
end
