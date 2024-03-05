import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { Button } from '@mui/material';
import Grid from '@mui/material/Grid';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'fullname', headerName: 'Full Name', width: 210, editable: true,},
  { field: 'email', headerName: 'Email', width: 210, editable: true, },
  { field: 'mobile', headerName: 'Mobile', type: 'number', width: 210, editable: true, },
  { field: 'gender', headerName: 'Gender', width: 210, editable: true, },
  { field: 'dept_name', headerName: 'Department', width: 210, editable: true,},
  { field: 'hire_date', headerName: 'Hire Date', width: 210, editable: true,},
  { field: 'permanent_employee', headerName: 'Permanent Employee', width: 210, editable: true,}
];

export default function EmpTable() {

  const [rows, setRows] = useState([]);
  const [selectedRowId, setSelectedRowId] = useState([]);

  // const [selectionModel, setSelectionModel] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/get_all_emp')
      .then(response => {
        setRows(response.data); 
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const deleteEmployee = () => {
    axios.get('http://127.0.0.1:8000/delete_emp_by_id/' + selectedRowId[0])
      .then(response => {
        setRows((prevRows)=> prevRows.filter((row)=>row.id !== selectedRowId[0])); 
      }).catch(error => {
        console.error('Error fetching data:', error);
      });
  };

  return (
    <>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Box sx={{ height: 400, width: '100%' }}>
            <DataGrid
              rows={rows}
              columns={columns}
              onRowSelectionModelChange={(ids) => setSelectedRowId(ids)}
              // selectionModel={selectionModel}
              initialState={{
                pagination: {
                  paginationModel: {
                    pageSize: 5,
                  },
                },
              }}
              pageSizeOptions={[5]}
              checkboxSelection
              disableRowSelectionOnClick
            />
          </Box>
        </Grid>
        <Grid item xs={12}>
          <div>
            <Button 
              variant="contained" 
              onClick={deleteEmployee} 
              color="error"  
              type="button" 
              style={{ marginRight: "8px" }}
            >Delete Employee
            </Button>
          </div>
        </Grid>
      </Grid>
    </>
  );
}
