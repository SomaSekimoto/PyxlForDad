<template>
  <div>
    <h1>{{ msg }}</h1>
    <p>拡張子.xlsxのファイル</p>
    <input type="file" @change="readFile" />
  </div>
  <!-- <button style="margin: 3em;" @click="uploadFile">アップロード</button> -->
</template>

<script>
import axios from "axios";
export default {
  name: "Upload",
  props: {
    msg: String
  },
  data: () => ({}),
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
      // const headers = { "content-type": "multipart/form-data" };
      axios
        // .post(path, data, { headers })
        .post(path, data)
        .then(res => {
          console.log("res");
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
