const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const list = document.getElementById('todo-list');

// 할 일 목록 상태. 추가한 순서대로 보관한다.
let todos = [];

function render() {
  list.innerHTML = '';

  todos.forEach((todo) => {
    const item = document.createElement('li');
    item.className = 'todo-item';
    item.textContent = todo.text; // innerHTML 대신 textContent로 넣어 HTML 주입을 막는다.
    list.appendChild(item);
  });
}

function addTodo(rawText) {
  const text = rawText.trim();

  // 빈 문자열이나 공백만 있는 입력은 경고 없이 무시한다.
  if (text === '') {
    return false;
  }

  todos.push({ id: Date.now(), text });
  render();
  return true;
}

// form submit으로 처리하면 "추가" 버튼 클릭과 Enter 입력을 모두 받을 수 있다.
form.addEventListener('submit', (event) => {
  event.preventDefault();

  if (addTodo(input.value)) {
    input.value = '';
  }

  input.focus();
});

render();
