
{% for book in site.data.researchmap %}
{% assign d = book[0] %}

1. {{ d }}
2. {{ d | id }}
3. {{ d.insert.merge }}
4. {{ d | book_title }}
5. {{ d.insert.merge.book_title.ja }}

- {{ book.book_title }}　({{ book.authors }})

1. {{ book | insert }}
1. {{ book.insert }}
1. {{ book.insert.id}}
1. {{ book.user_id}}
1. {{ book.merge.book_title.ja}}

{% endfor %}


{"insert":    {
        "type":"books_etc",
        "id":"9614893",
        "user_id":"B000001034"},
        "merge":
            {   "display":"disclosed",
                "major_achievement":false,
                "book_title":{
                    "ja":"白井博士の未来のゲームデザイン -エンターテインメントシステムの科学-"},
                    "book_owner_role":"single_work",
                    "authors":{
                        "ja":[{
                            "name":"白井 暁彦"},
                            {"name":"はやのん"}]},
                            "publisher":{
                                "ja":"ワークスコーポレーション"},
                                "publication_date":"2013-11-26",
                                "total_page":"192",
                                "referee":false,
                                "identifiers":{
                                    "isbn":["4862671586"],
                                    "asin":["4862671586"],
                                    "ean":["9784862671585"],
                                    "cinii_nc_id":["BB1405576X"]},
                                    "see_also":[{
                                        "label":"cinii_books",
                                        "@id":"http://ci.nii.ac.jp/ncid/BB1405576X",
                                        "is_downloadable":false
                                        },
                                        {
                                            "label":"amazon_url",
                                            "@id":"https://www.amazon.co.jp/%E7%99%BD%E4%BA%95%E5%8D%9A%E5%A3%AB%E3%81%AE%E6%9C%AA%E6%9D%A5%E3%81%AE%E3%82%B2%E3%83%BC%E3%83%A0%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3-%E3%82%A8%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%86%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%B3%E3%83%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%AE%E7%A7%91%E5%AD%A6-%E7%99%BD%E4%BA%95-%E6%9A%81%E5%BD%A6/dp/4862671586%3FSubscriptionId%3DAKIAJGNOIQQZDD6XM6QQ%26tag%3Dresearchmap21-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4862671586"},
                                            {
                                                "label":"amazon_small_image_url",
                                                "@id":"https://images-fe.ssl-images-amazon.com/images/I/51-InvXHz%2BL._SL75_.jpg"},
                                                {
                                                    "label":"amazon_medium_image_url","@id":"https://images-fe.ssl-images-amazon.com/images/I/51-InvXHz%2BL._SL160_.jpg"
                                                },
                                                {"label":"amazon_large_image_url","@id":"https://images-fe.ssl-images-amazon.com/images/I/51-InvXHz%2BL.jpg"}]}}
{"insert":{"type":"books_etc","id":"23141","user_id":"B000001034"},"merge":{"display":"disclosed","major_achievement":false,"book_title":{"ja":"WiiRemoteプログラミング"},"book_owner_role":"joint_work","authors":{"ja":[{"name":"白井 暁彦"},{"name":"小坂 崇之"},{"name":"くるくる研究室"},{"name":"木村 秀敬"},{"name":"オーム社開発部"},{"name":"タナカユカリ"}]},"publisher":{"ja":"オーム社"},"publication_date":"2009-07-25","total_page":"400","referee":false,"identifiers":{"isbn":["4274067505"],"asin":["4274067505"],"ean":["9784274067501"]},"see_also":[{"label":"amazon_url","@id":"https://www.amazon.co.jp/WiiRemote%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E7%99%BD%E4%BA%95-%E6%9A%81%E5%BD%A6/dp/4274067505%3FSubscriptionId%3DAKIAJGNOIQQZDD6XM6QQ%26tag%3Dresearchmap21-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4274067505"},{"label":"amazon_small_image_url","@id":"https://images-fe.ssl-images-amazon.com/images/I/51dt1H-3WKL._SL75_.jpg"},{"label":"amazon_medium_image_url","@id":"https://images-fe.ssl-images-amazon.com/images/I/51dt1H-3WKL._SL160_.jpg"},{"label":"amazon_large_image_url","@id":"https://images-fe.ssl-images-amazon.com/images/I/51dt1H-3WKL.jpg"}]}}
