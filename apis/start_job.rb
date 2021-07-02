# job startサンプル
api_key = ENV['API_KEY']
params = {project: ENV['PROJECT_ID'], spider: :basic_auth}
req = Faraday::Connection.new(url: "https://app.scrapinghub.com/api/run.json") do |conn|
  conn.adapter Faraday.default_adapter
  conn.request :url_encoded
  conn.response :logger
  conn.headers['Accept'] = 'application/json'
  conn.basic_auth(api_key, '')
end
res = req.post('', params.to_query)
pp JSON.parse(res.body)
