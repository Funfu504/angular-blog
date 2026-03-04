from blogservicepkg.db import get_post_table

def test_table_has_data():
    table = get_post_table()
    assert table.item_count == 6