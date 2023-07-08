document.addEventListener('DOMContentLoaded', function() {
  const categoryField = document.querySelector('#id_category');
  const damageField = document.querySelector('#id_damage');
  const strField = document.querySelector('#id_str');
  const dexField = document.querySelector('#id_dex');
  const attackTypeField = document.querySelector('#id_attack_type');

  // Функция для обновления формы в зависимости от выбранной категории
  function updateFormFields() {
    if (categoryField.value === 'weapon') {
      damageField.parentNode.style.display = 'block';
      strField.parentNode.style.display = 'block';
      dexField.parentNode.style.display = 'block';
      attackTypeField.parentNode.style.display = 'block';
    } else {
      damageField.parentNode.style.display = 'none';
      strField.parentNode.style.display = 'none';
      dexField.parentNode.style.display = 'none';
      attackTypeField.parentNode.style.display = 'none';
    }
  }

  // Вызов функции при загрузке страницы и при изменении значения поля категории
  updateFormFields();
  categoryField.addEventListener('change', updateFormFields);
});