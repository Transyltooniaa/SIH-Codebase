<template>

  <b-card body-class="p-0" header-class="border-0">
    <template v-slot:header>
      <b-row align-v="center">
        <b-col>
          <h3 class="mb-0">Writing Summary</h3>
        </b-col>
        <b-col class="text-right">
          <a href="#!" class="btn btn-sm btn-primary">See all</a>
        </b-col>
      </b-row>
    </template>

    <el-table class="table-responsive table"
              :data="tableData"
              header-row-class-name="thead-light">
      <el-table-column label="Page name"
                       min-width="130px"
                       prop="page">
        <template v-slot="{row}">
          <div class="font-weight-600">{{row.page}}</div>
        </template>
      </el-table-column>
      <el-table-column label="Visitors"
                       min-width="70px"
                       prop="visitors">
      </el-table-column>
      <el-table-column label="Unique users"
                       min-width="90px"
                       prop="unique">
      </el-table-column>

      <el-table-column label="Bounce rate"
                       min-width="90px"
                       prop="bounceRate">
        <template v-slot="{row}">
          {{row.bounceRate}}
        </template>
      </el-table-column>
    </el-table>
  </b-card>
</template>
<script>
  import { Table, TableColumn, DropdownMenu, DropdownItem, Dropdown} from 'element-ui'
  export default {
    name: 'page-visits-table',
    components: {
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
            page: 'Mathematics-1',
            visitors: '700',
            unique: '36',
            bounceRate: '63%'
          },
          {
            page: 'Social Science',
            visitors: '670',
            unique: '34',
            bounceRate: '60%'
          },
          {
            page: 'History',
            visitors: '584',
            unique: '30',
            bounceRate: '62%'
          },
          {
            page: 'Practice Session - II',
            visitors: '576',
            unique: '28',
            bounceRate: '58%'
          },
          {
            page: 'Practice Session - I',
            visitors: '620',
            unique: '30',
            bounceRate: '53%'
          }
        ]
      }
    }
  }
</script>
<style>
</style>
 