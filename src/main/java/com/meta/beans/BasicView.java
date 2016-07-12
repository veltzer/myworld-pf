package com.meta.beans;

import java.io.Serializable;
import java.util.List;
import java.util.logging.Logger;

import javax.annotation.PostConstruct;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.ManagedProperty;
import javax.faces.bean.SessionScoped;
 
@SuppressWarnings("serial")
@ManagedBean(name="dtBasicView")
@SessionScoped
public class BasicView implements Serializable {
	
	private final Logger log =
	          Logger.getLogger(this.getClass().getName());
     
    private List<Car> cars;
    String carId;

    public String getCarId() {
		return carId;
	}

	public void setCarId(String carId) {
		log.info("setting car id to "+carId);
		this.carId = carId;
	}

	@ManagedProperty("#{carService}")
    private CarService service;
 
    @PostConstruct
    public void init() {
        cars = service.createCars(10);
    }
     
    public List<Car> getCars() {
        return cars;
    }
 
    public void setService(CarService service) {
        this.service = service;
    }
    
    public Car getCarById(String id) {
    	log.info("searching for carid "+this+", "+id);
    	for(Car c:cars) {
    		if(c.getId().equals(id)) {
    			return c;
    		}
    	}
    	log.info("returning null");
    	return null;
    }
    public Car getCurrentCar() {
    	return getCarById(carId);
    }
}
