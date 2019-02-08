const btnDelete = document.querySelectorAl('.btn-delete')

if(btnDelete){
    const  btnArray =Array.from(btnDelete);
    btnArray.forEaach((btn) =>{
    btn.addEventListener('click',(e)=> {
        if (!confirm('Are you sure want to delete it?')) {
            e.preventDefault();
        }
    });
});