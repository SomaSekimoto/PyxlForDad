<template>
  <div>
    <h1>{{ msg }}</h1>
    <p>拡張子.xlsxのファイル</p>
    <input type="file" @change="readFile" accept=".xlsx, .xls" />
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Upload",
  props: {
    msg: String
  },
  methods: {
    readFile(e) {
      const reader = new FileReader();
      const file = e.target.files[0];
      reader.onload = e => {
        this.uploadFile(e.target.result);
      };
      reader.readAsDataURL(file);
    },
    uploadFile(file) {
      const path = "http://localhost:5000/upload";
      const data = new FormData();
      data.append("file", file);
      const headers = { responseType: "blob", dataType: "binary" };
      axios
        .post(path, data, headers)
        .then(res => {
          console.log("res");
          console.log(res);
          const type =
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";
          const fileURL = window.URL.createObjectURL(
            new Blob([res.data], { type: type })
          );
          const fileLink = document.createElement("a");
          fileLink.href = fileURL;
          const dateString = new Date().toLocaleDateString("ja-jp");
          fileLink.setAttribute("download", dateString + ".xlsx");
          fileLink.click();
        })
        .catch(err => {
          console.log("err");
          console.log(err);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
