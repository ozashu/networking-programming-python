% include('form.tpl')
  <h2>検索結果</h2>
  <ul class=entries>
% if keyword in article_title:
    % for entry in article_title:
        <li><img src={{ entry['user_image'] }} width="50" height="50">
        <a href="{{ entry['url'] }}"> {{ entry['title'] }} </a> : <a href="https://qiita.com/{{ entry['user_id'] }}"> {{ entry['user_id'] }} </a>
% elif keyword in searched_user_id:
    % for entry in searched_user_id:
        <li><img src={{ entry['user_image'] }} width="50" height="50">
        <a href="{{ entry['url'] }}"> {{ entry['title'] }} </a> : <a href="https://qiita.com/{{ entry['user_id'] }}"> {{ entry['user_id'] }} </a>

% else:
    <li><em>Unbelievable.  No articles here so far</em>
% end
  </ul>
