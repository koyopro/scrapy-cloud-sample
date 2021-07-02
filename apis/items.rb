# item一覧取得サンプル
api_key = ENV['API_KEY']
job_key = ENV['JOB_KEY']
req = Faraday::Connection.new(url: "https://storage.scrapinghub.com/items/#{job_key}/?count=10") do |conn|
  conn.adapter Faraday.default_adapter
  conn.request :url_encoded
  conn.response :logger
  conn.headers['Accept'] = 'application/json'
  conn.basic_auth(api_key, '')
end
res = req.get('')
pp JSON.parse(res.body)
