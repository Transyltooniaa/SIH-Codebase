<template>
  <div class="input-container">
    <textarea
      v-model="inputText"
      placeholder="Type Hello..."
      class="text-input"
    ></textarea>
    
    <!-- Button to fetch recommendations -->
    <button class="fetch-button" @click="updateSuggestions">Get Suggestions</button>
    
    <div v-if="suggestions.length" class="suggestions-container">
      <div
        v-for="(suggestion, index) in suggestions"
        :key="index"
        class="suggestion"
        @click="completeSentence(suggestion)"
      >
        {{ suggestion }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      inputText: '',   // To store the user's input
      suggestions: [], // To store the suggestions fetched from the backend
    };
  },
  methods: {
    async updateSuggestions() {
      if (this.inputText.trim().length === 0) {
        this.suggestions = [];
        return;
      }

      // Send the latest inputText to the backend for recommendations
      try {
        const response = await axios.post('http://127.0.0.1:8000/generate_recommendations/', {
          input_sentence: this.inputText, // Send the entire text
        });

        // Update suggestions from the backend response
        this.suggestions = response.data.recommendations.split('.').filter(s => s.trim().length > 0);
      } catch (error) {
        console.error('Error fetching recommendations:', error);
        this.suggestions = [];
      }
    },
    completeSentence(suggestion) {
      // Replace the last incomplete word with the selected suggestion
      const words = this.inputText.split(' ');
      words.pop(); // Remove the last word (the incomplete one)
      
      // Append the selected suggestion to complete the sentence
      this.inputText = words.join(' ') + ' ' + suggestion;
      
      // Clear the suggestions after the sentence is completed
      this.suggestions = [];
    },
  },
  watch: {
    // Watch for changes in inputText and update suggestions accordingly
    inputText() {
      this.updateSuggestions(); // Automatically fetch suggestions after every update
    }
  }
};
</script>

<style scoped>
.input-container {
  perspective: 1000px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  height: 100vh;
}

.text-input {
  margin-top: 20px;
  width: 80vw;
  height: 60vh;
  padding: 10px;
  border: none;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2), 0 2px 5px rgba(0, 0, 0, 0.2);
  font-size: 30px;
  line-height: 1.2;
  text-align: left;
  display: block;
  overflow-y: auto;
  box-sizing: border-box;
  transition: transform 0.2s;
  resize: none;
}

.text-input:focus {
  outline: none;
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3), 0 3px 7px rgba(0, 0, 0, 0.3);
}

.suggestions-container {
  margin-top: 10px;
  width: 80vw;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  max-height: 150px;
  overflow-y: auto;
}

.suggestion {
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid #eee;
}

.suggestion:hover {
  background-color: #e0e0e0;
}
</style>
