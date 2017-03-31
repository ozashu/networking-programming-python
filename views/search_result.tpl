include('form.tpl')
  <h2>検索結果</h2>
  <ul class=entries>
% if keyword != searched_result:
    % for entry in searched_result:
        <li><img src={{ entry['user_image'] }} width="50" height="50">
        <a href="{{ entry['url'] }}"> {{ entry['title'] }} </a> : <a href="https://qiita.com/{{ entry['user_id'] }}"> {{ entry['user_id'] }} </a>
    % end
% else:
    <li><em>Unbelievable.  No articles here so far</em>
% end
  </ul>
