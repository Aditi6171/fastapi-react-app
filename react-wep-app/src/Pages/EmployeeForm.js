import React, { useState } from "react";
import { FormControl, FormControlLabel, FormLabel, Grid, Radio, RadioGroup, TextField } from "@mui/material";
import { makeStyles } from '@mui/styles';
import Select from "../controls/Select";
import DatePick from "../controls/DatePick";
import * as employeeservice from "../Services/EmpService";
import Button from "@mui/material/Button";
import axios from "axios";
import Checkbox from "@mui/material/Checkbox";


const useStyles = makeStyles(theme=>({
    root:{
        '& .MuiFormControl-root':{
            width:'80%',
            margin: theme.spacing(1),

        }
    }
}));

const empObject={
    id: null,
    fullname:'',
    email:'',
    mobile:'',
    city:'',
    gender:'',
    dept_code:'',
    hire_date: new Date(),
    permanent_employee: false
};


export default function EmployeeForm({selectedId}){
    const [values, setValues] = useState(empObject);

     const [isChecked, setIsChecked] = useState(false);

    const classes = useStyles();
    const handleInputChange = e => {
        const{name, value} = e.target
        setValues({...values,[name]: value});
    };

    const handleReset = () => {
        setValues(empObject);
    }

    const handleRegister = async () => {
        console.log("Inside handleRegister ...")
        const permanentEmployeeValue = isChecked ? "yes" : "no";
        axios.post('http://127.0.0.1:8000/create_emp', {
            fullname: values.fullname,
            email: values.email,
            mobile: values.mobile,
            city: values.city,
            gender: values.gender,
            dept_code: values.dept_code,
            hire_date: values.hire_date,
            permanent_employee: permanentEmployeeValue
            }
        ).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        });
    };

   


    return(
        <form onSubmit={handleRegister}>
            <Grid container className={classes.root}>
                <Grid item xs={6}>
                    <TextField variant="outlined" label="Full Name" name="fullname" value={values.fullname} onChange={handleInputChange} autoComplete="off"/>
                    <TextField variant="outlined" label="Email" name="email" value={values.email} onChange={handleInputChange} autoComplete="off"/>
                    <TextField variant="outlined" label="Mobile" name="mobile" value={values.mobile} onChange={handleInputChange} autoComplete="off"/>
                    <TextField variant="outlined" label="City" name="city" value={values.city} onChange={handleInputChange} autoComplete="off"/>
                </Grid>
                <Grid item xs={6}>
                    <FormControl>
                        <FormLabel>Gender</FormLabel>
                        <RadioGroup row name="gender" value={values.gender} onChange={handleInputChange}>
                            <FormControlLabel value="male" control={<Radio/>} label="Male"/>
                            <FormControlLabel value="female" control={<Radio/>} label="Female"/>
                            <FormControlLabel value="other" control={<Radio/>} label="Other"/>
                        </RadioGroup>
                    </FormControl>
                    <Select name="dept_code" label="Department" value={values.dept_code} onChange={(e) => handleInputChange({ target: { name: 'dept_code', value: e.target.value } })} options={employeeservice.getDepartmentCollection()} />
                    <DatePick name="hire_date" label="Hire Date" value={values.hire_date} onChange={(date) => handleInputChange({ target: { name: 'hire_date', value: date } })}/>

                    <div style={{ marginBottom: "16px" }}>
                    <FormControlLabel control={<Checkbox />} label="Permanent Employee?"name="permanent_employee" onChange={() => setIsChecked((prev) => !prev)} checked={isChecked}/>
                    </div>

                    <div>
                        <Button variant="contained" color="success" type="submit" style={{ marginRight: "8px" }}>Submit</Button>
                        
                        <Button variant="contained" color="inherit" type="reset" onClick={handleReset}>Reset</Button>
                    </div>
                </Grid>
            </Grid>
        </form>
    );
}