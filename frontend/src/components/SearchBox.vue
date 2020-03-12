<template>
  <div id="searchbox">
    <template>

      <h1 >Best Search Engine</h1>
      <div class="input-group md-form form-sm form-2 pl-0">
        <input class="form-control my-0 py-1 black-border" type="text" placeholder="Search Paper" aria-label="Search">
          <div class="input-group-append">
            
            <mdb-btn color="mdb-color" rounded size="sm" type="submit" class="mr-auto" @click="getPaperResults">
              <mdbIcon icon="search"/>
            </mdb-btn>

          </div>
      </div>
    </template>
    {{searchResults}}
   
  </div>
</template>

<script>

import { mdbBtn, mdbIcon } from 'mdbvue';
import SearchPaperService from '../api/SearchPaperService'

export default {
    name: 'SearchBox',
    components: {

        mdbIcon,
        mdbBtn
    },
    data() {
            return {
                searchResults: null
            }
        },
    methods: {
        async getPaperResults () {
            SearchPaperService.searchPaper()
            .then(response => (this.searchResults = response.data))
        }
    }
}
</script>

<style>
#searchbox {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10%;
  margin-left: 25%;
  margin-right: 25%;
}
</style>
