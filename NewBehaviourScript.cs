﻿using UnityEngine;
using System.Collections;

// create game class
public class NewBehaviourScript : MonoBehaviour
{

    // create all variables 
    private Rigidbody2D myRigidbody;

    private bool facingRight;

    private Animator myAnimator;

    private bool punch;

    private bool isGrounded;

    private bool jump;

    public Transform fire_point;

    public GameObject NinjaStar_Projectile;

    [SerializeField] // SerializeField will allow to change variable parameters from Inspector in Unity
    private float movementSpeed;

    [SerializeField]
    private Transform[] groundPoints;

    [SerializeField]
    private float groundRadius;

    [SerializeField]
    private LayerMask whatIsGround;

    [SerializeField]
    private float jumpForce;

    [SerializeField]
    private bool airControl;



    // Use this for initialization
    void Start ()
    {
        // set all the components 
        facingRight = true;
        myRigidbody = GetComponent<Rigidbody2D>();
        myAnimator = GetComponent<Animator>();
	}

    // update everytime 
    void Update()
    {
        HandleInput();
    }
	

	// Update is called once per frame
	void FixedUpdate()
    {
        float horizontal = Input.GetAxis("Horizontal");

        HandleMovement(horizontal);
        HandleAttacks();
        ResetValues();
        Flip(horizontal);
        isGrounded = IsGrounded();
	
	}

    // handles all the movement 
    private void HandleMovement(float horizontal)

    {
        if (!this.myAnimator.GetCurrentAnimatorStateInfo(0).IsTag("Punch"))
        {
            myRigidbody.velocity = new Vector2(horizontal * movementSpeed, myRigidbody.velocity.y);
        }
        myAnimator.SetFloat("speed", Mathf.Abs(horizontal));

        if (isGrounded && jump)
        {
            isGrounded = false;
            myRigidbody.AddForce(new Vector2(0, jumpForce));
        }



    }

    // handle attack 
    private void HandleAttacks()
    {
        if (punch && !this.myAnimator.GetCurrentAnimatorStateInfo(0).IsTag("Punch"))
        {
            myAnimator.SetTrigger("punch");
            myRigidbody.velocity = Vector2.zero;
        }
    }

    // handle all the keyboard inputs
    private void HandleInput()
    {
        if (Input.GetKeyDown(KeyCode.E))
        {
            punch = true;
        }
        if (Input.GetKeyDown(KeyCode.W))
        {
            jump = true;
        }
        if (Input.GetKeyDown(KeyCode.Q))
        {
            Instantiate(NinjaStar_Projectile, fire_point.position, fire_point.rotation);
        }

    }

    // handle the fliping of the character from left - right
    private void Flip(float horizontal)
    {
        if (horizontal > 0 && !facingRight || horizontal < 0 && facingRight)
        {
            facingRight = !facingRight;

            Vector3 theScale = transform.localScale;
            theScale.x *= -1;
            transform.localScale = theScale;
        }
    }

    // handle reset values for the movements
    private void ResetValues()
    {
        punch = false;
        jump = false;
    }

    // handle the collision between ground and player
    private bool IsGrounded()
    {
        if (myRigidbody.velocity.y <= 0)
        {
            foreach (Transform point in groundPoints)
            {
                Collider2D[] colliders = Physics2D.OverlapCircleAll(point.position, groundRadius, whatIsGround);

                for (int i = 0; i < colliders.Length; i++)
                {
                    if (colliders[i].gameObject != gameObject)
                    {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
