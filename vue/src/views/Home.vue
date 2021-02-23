<template>
  <section class="images">
    <button v-on:click="open = !open" class="tags-filter">Tags</button>
    <div class="dropdown-wrapper" v-if="open == true">
      <div
        class="option"
        v-for="(tag, index) in tags"
        v-bind:key="index"
        v-on:click="selectTag(tag.name)"
      >
        {{ tag.name }}
      </div>
    </div>
    <button v-on:click="getImages()">Done</button>
  </section>
</template>

<style lang="scss">
.tags-filter {
  background: none;
  border: 2px solid black;
  padding: 15px 50px;
  cursor: pointer;
}
.dropdown-wrapper {
  border: 2px solid black;
  .option{
    cursor: pointer;
  }
}
</style>

<script>
// @ is an alias to /src
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      allImages: null,
      tags: [
        { name: "test" },
        { name: "test 1" },
        { name: "test 2" },
        { name: "test 3" },
      ],
      selectTags: [],
      open: false,
      tag:'',
    };
  },
  // mounted(){
  //   this.getImagesBytag(this.selectTags)
  // },

  methods: {
    // async getAllImages() {
    //   const response = await axios
    //     .get("/images")
    //     .then(function (response) {
    //       return response;
    //     })
    //     .catch(function (error) {
    //       console.log(error);
    //     });

    //   this.allImages = response.data.results;
    // },
    async getImagesBytag(SelectedTags) {
      const response = await axios({
        method: "get",
        url: "http://localhost:5000/images",
        headers: { "Content-type": "application/json" },
        data: {
          tags: SelectedTags,
        },
      })
        .then(function (response) {
          return response;
        })
        .catch(function (error) {
          console.log(error);
        });

      this.imagesByTags = response.data.results;
    },
    selectTag(tag) {
      this.selectTags.push(tag);
    },
    getImages(){
      this.getImagesBytag(this.selectTags)
    }
  },
};
</script>
