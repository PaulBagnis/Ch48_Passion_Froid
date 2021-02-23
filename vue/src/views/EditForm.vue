<template>
  <section class="edit-form">
    <form action="">
      <label for="name">Name</label>
      <input type="text" name="name" v-model="name" />
      <br />
      <label for="choice-radio"
        >Photo avec produit
        <input type="radio"
        name="choice-radio" 
        value="yes"
        v-model="productImage"/>
        Oui
        <input
        type="radio"
        name="choice-radio"
        value="no"
        v-model="productImage"/>
        Non
      </label>
      <br />
      <label for="choice-radio"
        >Photo avec humain
        <input type="radio"
        name="choice-radio"
        value="yes"
        v-model="humanImage"/>
        Oui
        <input 
        type="radio" 
        name="choice-radio"
        value="no"
        v-model="humanImage"/>
        Non
      </label>
      <br />
      <label for="choice-radio"
        >Photo institutionelle
        <input type="radio"
         name="choice-radio"
         value="yes"
         v-model="institutionnalImage"/>
        Oui
        <input 
        type="radio" 
        name="choice-radio"
        value="no"
        v-model="institutionnalImage"/>
        Non
      </label>
      <label for="choice-radio"
        >Format
        <input 
        type="radio" 
        name="choice-radio" 
        value="horizontal"
        v-model="format"/>
        Horizontal
        <input 
        type="radio" 
        name="choice-radio"
        value="vertical"
        v-model="format"/>
        Vertical
      </label>
      <br />
      <label for="credit">Crédit</label>
      <input 
      type="text"
      v-model="credits"
       />
      <br />
      <label for="tags">Tags</label>
      <input 
      type="text"
      v-model="tags" />
      <br>
      <br>
      <label for="choice-radio"
      >Droit d'utilisations limités
      <input 
      value="yes" 
      v-model="limitedUsage" 
      type="radio" 
      name="choice-radio" />
      Oui
      <input 
      value="no" 
      v-model="limitedUsage" 
      type="radio" 
      name="choice-radio" />
      Non
    </label>
    <br>
    <br>
    <div v-if="limitedUsage == 'yes'">
      <label for="tags">Copyright</label>
      <input 
      type="text"
      v-model="copyright">
    </div>
    <br>
    <div v-if="limitedUsage == 'yes'">
      <label for="date"> Date de fin de droits d'utilisation </label>
      <input 
      v-model="limitedUsage" 
      value="yes" 
      type="date" 
      name="date" >
    </div>
    <br>
    <label for="tags">Tags</label>
    <input type="text" name="tags">
    <br>
    <br>
    <input type="submit" value="Entrez">
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
      tags: [],
      right: Boolean,
      response: Boolean
    }
  },
  methods:{}

}
</script>

<style>

</style>