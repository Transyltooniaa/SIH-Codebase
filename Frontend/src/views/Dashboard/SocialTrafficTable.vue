<template>
  <b-card body-class="p-0" header-class="border-0">
    <template v-slot:header>
      <b-row align-v="center">
        <b-col>
          <h3 class="mb-0" style="white-space: nowrap;">Practice Sets Completed</h3>
        </b-col>
        <b-col class="text-right">
          <base-button size="sm" type="primary">See all</base-button>
        </b-col>
      </b-row>
    </template>

    <el-table
      class="table-responsive table"
      :data="tableData"
      header-row-class-name="thead-light"
    >
      <el-table-column min-width="180px" prop="name">
        <template v-slot="{ row }">
          <div class="font-weight-bold" style="padding: 8px; white-space: nowrap;">{{ row.name }}</div>
        </template>
      </el-table-column>

      <el-table-column min-width="250px" prop="progress">
        <template v-slot="{ row }">
          <div class="d-flex align-items-center" style="min-width: 250px; justify-content: space-between;">
            <span class="mr-2" style="font-weight: 600;">{{ row.progress }}%</span>
            <base-progress :type="row.progressType" :value="row.progress" style="flex-grow: 1; margin-left: 10px;" />
          </div>
        </template>
      </el-table-column>
    </el-table>
  </b-card>
</template>

<script>
  import { BaseProgress } from '@/components';
  import { Table, TableColumn, DropdownMenu, DropdownItem, Dropdown} from 'element-ui'
  export default {
    name: 'social-traffic-table',
    components: {
      BaseProgress,
      [Table.name]: Table,
      [TableColumn.name]: TableColumn,
      [Dropdown.name]: Dropdown,
      [DropdownItem.name]: DropdownItem,
      [DropdownMenu.name]: DropdownMenu,
    },
    data() {
      return {
        tableData: [
        {
          name: 'Focus Duration',
          score: '45 mins',
          progress: 70,
          progressType: 'gradient-info',
        },
        {
          name: 'Sentence Complexity',
          score: 'Intermediate',
          progress: 65,
          progressType: 'gradient-primary',
        },
        {
          name: 'Vocabulary Usage',
          score: '100 unique words',
          progress: 80,
          progressType: 'gradient-success',
        },
        {
          name: 'Assistive Tool Usage',
          score: '30 times',
          progress: 50,
          progressType: 'gradient-warning',
        },
        {
          name: 'Text Comprehension ',
          score: '90%',
          progress: 90,
          progressType: 'gradient-success',
        }
      ]

      }
    }

  }
</script>
<style>
</style>
