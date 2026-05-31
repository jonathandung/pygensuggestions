from pygensuggestions.lib import suggest
def test_basic_suggestion(): assert suggest(['apple', 'apricot', 'banana', 'grape'], 'appple') == 'apple'
def test_case_insensitive_suggestion(): assert suggest(['Python', 'Java', 'JavaScript', 'Ruby'], 'python') == 'Python'
def test_empty_candidates(): assert suggest([], 'test') is None
def test_item_not_in_candidates():
    candidates = {'cat', 'bat', 'rat', 'mat'}
    result = suggest(candidates, 'hat')
    assert result in candidates
    assert result != 'hat'
def test_max_candidate_items_limit(): assert suggest([f'item_{i}' for i in range(751)], 'test') is None
def test_string_too_long(): assert suggest(['short', 'medium'], 'x'*41) is None
def test_multiple_similar_candidates():
    candidates = ['receive', 'recieve', 'recept', 'recent']
    result = suggest(candidates, 'recieve')
    assert result in {'receive', 'recieve'}
def test_all_strings_very_different():
    candidates = {'one', 'two', 'three', 'four'}
    result = suggest(candidates, 'xxxxxxxxxxx')
    assert result in candidates
def test_with_numbers_and_mixed_types(): assert suggest(['123', '456', '789', '012'], '124') == '123'
def test_single_candidate():
    candidates = ['only_one']
    assert suggest(candidates, 'only_one') is None
    assert suggest(candidates, 'different') is candidates[0]
def test_suggestion_with_unicode(): assert suggest(['café', 'cafe', 'coffee', 'tea'], 'cafe') in {'cafe', 'café'}
def test_consecutive_calls():
    candidates = ['apple', 'apricot', 'avocado', 'banana']
    assert suggest(candidates, 'appple') == 'apple'
    assert suggest(candidates, 'bannana') == 'banana'
def test_identical_candidates(): assert suggest(['same', 'same', 'same', 'different'], 'sme') == 'same'
def test_whitespace_handling():
    candidates = ['hello world', 'helloworld', 'hello  world']
    assert suggest(candidates, 'hellowrld') in candidates
def test_dictionary_suggestion():
    dictionary = ['accommodation', 'accomodation', 'accomodate', 'recommend', 'recmmend', 'recomend']
    assert suggest(dictionary, 'accomodation') == 'accommodation'
    assert suggest(dictionary, 'recmmend') == 'recommend'
def test_programming_keywords():
    keywords = ['break', 'def', 'class', 'return', 'import', 'from']
    assert suggest(keywords, 'defg') == 'def'
    assert suggest(keywords, 'clas') == 'class'
    assert suggest(keywords, 'retrun') == 'return'
def test_file_extensions():
    extensions = ['.py', '.js', '.html', '.css', '.json', '.xml']
    assert suggest(extensions, '.pY') == '.py'
    assert suggest(extensions, '.htm') == '.html'
def test_case_insensitive_search():
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    assert suggest(colors, 'red') == 'Red'
    assert suggest(colors, 'BLUE') == 'Blue'
def test_basic_suggestion_bytes(): assert suggest([b'apple', b'apricot', b'banana', b'grape'], b'appple') == b'apple'
def test_case_insensitive_suggestion_bytes(): assert suggest([b'Python', b'Java', b'JavaScript', b'Ruby'], b'python') == b'Python'
def test_empty_candidates_bytes(): assert suggest([], b'test') is None
def test_item_not_in_candidates_bytes():
    candidates = {b'cat', b'bat', b'rat', b'mat'}
    result = suggest(candidates, b'hat')
    assert result in candidates
    assert result != b'hat'
def test_max_candidate_items_limit_bytes(): assert suggest(tuple(map(b'item_%d'.__mod__, range(751))), b'test') is None
def test_string_too_long_bytes(): assert suggest([b'short', b'medium'], b'x'*41) is None
def test_multiple_similar_candidates_bytes():
    candidates = [b'receive', b'recieve', b'recept', b'recent']
    result = suggest(candidates, b'recieve')
    assert result in {b'receive', b'recieve'}
def test_all_strings_very_different_bytes():
    candidates = {b'one', b'two', b'three', b'four'}
    result = suggest(candidates, b'xxxxxxxxxxx')
    assert result in candidates
def test_with_numbers_and_mixed_types_bytes(): assert suggest([b'123', b'456', b'789', b'012'], b'124') == b'123'
def test_single_candidate_bytes():
    candidates = [b'only_one']
    assert suggest(candidates, b'only_one') is None
    assert suggest(candidates, b'different') is candidates[0]
def test_consecutive_calls_bytes():
    candidates = [b'apple', b'apricot', b'avocado', b'banana']
    assert suggest(candidates, b'appple') == b'apple'
    assert suggest(candidates, b'bannana') == b'banana'
def test_identical_candidates_bytes(): assert suggest([b'same', b'same', b'same', b'different'], b'sme') == b'same'
def test_whitespace_handling_bytes():
    candidates = [b'hello world', b'helloworld', b'hello  world']
    assert suggest(candidates, b'hellowrld') in candidates
def test_dictionary_suggestion_bytes():
    dictionary = [b'accommodation', b'accomodation', b'accomodate', b'recommend', b'recmmend', b'recomend']
    assert suggest(dictionary, b'accomodation') == b'accommodation'
    assert suggest(dictionary, b'recmmend') == b'recommend'
def test_programming_keywords_bytes():
    keywords = [b'break', b'def', b'class', b'return', b'import', b'from']
    assert suggest(keywords, b'defg') == b'def'
    assert suggest(keywords, b'clas') == b'class'
    assert suggest(keywords, b'retrun') == b'return'
def test_file_extensions_bytes():
    extensions = [b'.py', b'.js', b'.html', b'.css', b'.json', b'.xml']
    assert suggest(extensions, b'.pY') == b'.py'
    assert suggest(extensions, b'.htm') == b'.html'
def test_case_insensitive_search_bytes():
    colors = [b'Red', b'Green', b'Blue', b'Yellow']
    assert suggest(colors, b'red') == b'Red'
    assert suggest(colors, b'BLUE') == b'Blue'