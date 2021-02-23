<template>
  <section class="add-form">
    <form action="">
      <label for="name">Name</label>
      <input type="text" name="name" v-model="name" />
      <br />
      <br />
      <label for="choice-radio"
        >Photo avec produit
        <input
          type="radio"
          name="choice-radio"
          value="yes"
          v-model="productImage"
        />
        Oui
        <input
          type="radio"
          name="choice-radio"
          value="no"
          v-model="productImage"
        />
        Non
      </label>
      <br />
      <br />
      <label for="choice-radio"
        >Photo avec humain
        <input
          type="radio"
          name="choice-radio"
          value="yes"
          v-model="humanImage"
        />
        Oui
        <input
          type="radio"
          name="choice-radio"
          value="no"
          v-model="humanImage"
        />
        Non
      </label>
      <br />
      <br />
      <label for="choice-radio"
        >Photo institutionelle
        <input
          type="radio"
          value="yes"
          name="choice-radio"
          v-model="institutionnalImage"
        />
        Oui
        <input
          type="radio"
          value="no"
          name="choice-radio"
          v-model="institutionnalImage"
        />
        Non
      </label>
      <br />
      <br />
      <label for="choice-radio"
        >Format
        <input
          type="radio"
          value="Horizontal"
          name="choice-radio"
          v-model="format"
        />
        Horizontal
        <input
          type="radio"
          value="Vertical"
          name="choice-radio"
          v-model="format"
        />
        Vertical
      </label>
      <br />
      <br />
      <label for="credit">Crédit</label>
      <input type="text" />
      <br />
      <br />
      <label for="tags">Tags</label>
      <input type="text" v-model="tag"/>
      <button v-on:click="addNewTag()">+</button>
      <div v-for="(tag,index) in tags" v-bind:key="index">{{tag.name}}</div>
      <br />
      <br />
      <label for="choice-radio"
        >Droits d'utilisations limités
        <input
          type="radio"
          value="yes"
          name="choice-radio"
          v-model="limitedUsage"
        />
        Oui
        <input
          type="radio"
          value="no"
          name="choice-radio"
          v-model="limitedUsage"
        />
        Non
      </label>
      <br />
      <br />
      <label for="tags" v-if="limitedUsage == 'yes'">Copyrights</label>
      <input type="text" v-if="limitedUsage == 'yes'" />
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      name: null,
      productImage: null,
      humanImage: null,
      institutionnalImage: null,
      format: null,
      credits: null,
      limitedUsage: null,
      copyright: null,
      UsageDate: null,
      tag:'',
      tags: [],
    };
  },
  methods:{
    addNewTag:function(){
      this.tags.push({name : this.tag})
    }
  }
};
</script>

<style>
</style>
