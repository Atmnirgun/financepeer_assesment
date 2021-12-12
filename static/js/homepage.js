
function getFile(){
   var file = document.querySelector('input[type="file"]')
   
   const formData = new FormData()
   formData.append("file",file.files[0])
   console.log(formData.get("file"));
   
   var url = "api/upload"
   params = {
      method : 'POST',
      body : formData
   }

   fetch(url, params).then((response) => {
      return response.json();
   }).then((result) => {
      if(result["status"]=="success"){
         let id = document.getElementById("form_div")
         id.classList.add("d-none")
         let message_block = document.getElementById('success_feedback')
         message_block.classList.remove("d-none")
         document.getElementById("success_feedback").textContent = "File Successfully Uploaded."
         let show_button = document.getElementById("show_btn")
         show_button.classList.remove("d-none")
     }
     if (result["status"]=="failed"){
         let id = document.getElementById("success_feedback")
         id.classList.remove("d-none")
         id.textContent = "Upload Failed."
     }
   });
}

