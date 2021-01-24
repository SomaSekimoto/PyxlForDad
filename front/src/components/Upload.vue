<template>
  <div>
    <h1>{{ msg }}</h1>
    <p>拡張子.xlsxのファイル</p>
    <input type="file" @change="uploadFile" />
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
    uploadFile(e) {
      console.log("aaa");
      console.log(e.target.files[0]);
      axios.get("/fetch", { params: e.target.files[0] });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
