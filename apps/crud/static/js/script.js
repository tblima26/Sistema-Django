const form = document.querySelector('form')
const maskCpf = document.querySelector('#cpf')
const maskTel = document.querySelector('#telefone')


maskCpf.addEventListener('input', (e) => {
  e.target.value = e.target.value
    .replace(/\D/g, '')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d)/, '$1.$2')
    .replace(/(\d{3})(\d{1,2})$/, '$1-$2')
    .substring(0, 14)
})

maskTel.addEventListener('input', (e) => {
  e.target.value = e.target.value
    .replace(/\D/g, '')
    .replace(/(\d{5})(\d{4})$/, '$1-$2')
    .replace(/^(\d{2})(\d)/g, '($1) $2')
    .substring(0, 15)
})